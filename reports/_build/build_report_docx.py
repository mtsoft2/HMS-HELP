"""
Build a single DOCX of every documented module on the HMS Help site.

Differences from build_report.py:
  * Word (.docx) output instead of PDF.
  * Real Word table-of-contents (pandoc --toc) that Word will update on F9.
  * Cover page rendered as a plain centred title page (no gradient — DOCX
    doesn't support CSS).
  * Every emoji stripped.
  * Every horizontal rule (`---` / `***`) stripped.
  * Hard page-break before each chapter (Pandoc converts our marker to
    a real Word page break).

Output:
  E:\\Work\\HMS-HELP\\reports\\HMS-Help-Full.docx
"""

from __future__ import annotations

import datetime as _dt
import re
import subprocess
import sys
from pathlib import Path

ROOT  = Path(r"E:/Work/HMS-HELP")
DOCS  = ROOT / "docs"
NAV   = ROOT / "mkdocs.yml"
OUT   = ROOT / "reports"
BUILD = OUT / "_build"
DOCX  = OUT / "HMS-Help-Full.docx"

# ---------------------------------------------------------------------- #
# Emoji + decorative-character ranges to strip (everything is removed,   #
# the surrounding text is kept).                                         #
# ---------------------------------------------------------------------- #
_EMOJI_RE = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"   # flags
    "\U0001F300-\U0001F5FF"   # symbols & pictographs
    "\U0001F600-\U0001F64F"   # emoticons
    "\U0001F680-\U0001F6FF"   # transport & map symbols
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"   # supplemental symbols & pictographs
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "☀-➿"           # misc symbols + dingbats
    "←-⇿"           # arrows  (←  →  ↳ etc.)
    "⌀-⏿"           # misc technical
    "①-⓿"           # enclosed alphanumerics
    "■-◿"           # geometric shapes
    "✀-➿"           # dingbats
    "︀-️"           # variation selectors
    "‍"                  # zero-width joiner
    "]+",
    flags=re.UNICODE,
)


# ---------------------------------------------------------------------- #
#  Parse mkdocs.yml nav                                                  #
# ---------------------------------------------------------------------- #
def parse_nav() -> list[tuple[int, str, Path | None]]:
    lines = NAV.read_text(encoding="utf-8").splitlines()
    in_nav = False
    out: list[tuple[int, str, Path | None]] = []

    for raw in lines:
        if raw.startswith("nav:"):
            in_nav = True
            continue
        if not in_nav:
            continue
        if raw and not raw[0].isspace():
            break

        stripped = raw.lstrip()
        if not stripped.startswith("-"):
            continue
        indent = (len(raw) - len(stripped)) // 2
        body = stripped[1:].strip()
        m = re.match(r"^([^:]+):\s*(.*)$", body)
        if not m:
            continue
        label, value = m.group(1).strip(), m.group(2).strip()
        if value:
            md = DOCS / value
            out.append((indent, label, md if md.exists() else None))
        else:
            out.append((indent, label, None))
    return out


# ---------------------------------------------------------------------- #
#  Sanitise the markdown                                                 #
# ---------------------------------------------------------------------- #
def _strip_decorations(text: str) -> str:
    # 1. Emojis
    text = _EMOJI_RE.sub("", text)

    # 2. MkDocs Material `:material-xxx:` and `:octicons-…:` icon refs.
    text = re.sub(r":material-[a-z0-9-]+:", "", text)
    text = re.sub(r":octicons-[a-z0-9-]+:", "", text)
    text = re.sub(r":fontawesome-[a-z0-9-]+:", "", text)

    # 3. Horizontal rule lines (--- or *** or ___ on a line by themselves,
    #    not inside YAML frontmatter — frontmatter was already stripped).
    text = re.sub(r"^\s*[-*_]{3,}\s*$\n?", "", text, flags=re.M)

    # 4. Collapse double blank lines created by the strips above.
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


# ---------------------------------------------------------------------- #
#  Build the combined markdown                                           #
# ---------------------------------------------------------------------- #
def build_combined_md(items) -> str:
    today = _dt.date.today().isoformat()

    cover = f"""---
title: "HMS Help - Combined Manual"
subtitle: "End-User and Administrator Manual"
author: "MT Soft"
date: "{today}"
toc: true
toc-depth: 3
toc-title: "Table of Contents"
---

\\newpage

# HMS Help

End-User and Administrator Manual for every module in the HMS Hospital Management System.

Generated {today}.

Source: https://mtsoft2.github.io/HMS-HELP/

Repository: https://github.com/mtsoft2/HMS-HELP

\\newpage

"""

    parts: list[str] = []

    for depth, label, md in items:
        if depth == 0 and md is None:
            parts.append(f"\n\\newpage\n\n# {label}\n\n")
            continue
        if md is None:
            continue
        try:
            content = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = md.read_text(encoding="utf-8", errors="replace")

        # Strip YAML front-matter
        content = re.sub(r"^---\n.*?\n---\n", "", content, count=1, flags=re.S)

        # Strip <style>...</style> blocks (home page has CSS)
        content = re.sub(r"<style[^>]*>.*?</style>", "", content, flags=re.S | re.I)

        # Strip HTML attribute markers like {.hms-section-title}
        content = re.sub(r"\s*\{[^}]+\}\s*$", "", content, flags=re.M)

        # Strip Material card grids (`<div class="grid cards"...>` blocks)
        # but keep the inner content.
        content = re.sub(r"<div[^>]*>", "", content)
        content = re.sub(r"</div>", "", content)

        # Rewrite relative image paths to absolute file:// so pandoc finds them.
        def _img(match):
            url = match.group(2)
            if re.match(r"^https?://", url):
                return match.group(0)
            abs_path = (md.parent / url).resolve()
            if abs_path.exists():
                return f"![{match.group(1)}]({abs_path.as_posix()})"
            return match.group(0)

        content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _img, content)

        # Strip MkDocs-Material `/// caption … ///` directives → italics
        content = re.sub(
            r"^/// caption\n(.*?)^///\s*$",
            lambda m: f"\n*{m.group(1).strip()}*\n",
            content,
            flags=re.S | re.M,
        )

        # Demote every heading by `depth` so nav hierarchy is preserved.
        if depth > 0:
            def _demote(m, d=depth):
                hashes = m.group(1) + "#" * d
                hashes = hashes[:6]
                return f"{hashes} {m.group(2)}"
            content = re.sub(r"^(#{1,6})\s+(.+)$", _demote, content, flags=re.M)

        # Final sanitisation pass (emojis, icons, HRs).
        content = _strip_decorations(content)

        parts.append(f"\n\\newpage\n\n{content}\n")

    combined = cover + "\n".join(parts)
    # One more global sweep so anything that snuck in via the cover is removed.
    combined = _strip_decorations(combined)
    return combined


# ---------------------------------------------------------------------- #
#  Main                                                                  #
# ---------------------------------------------------------------------- #
def main() -> int:
    BUILD.mkdir(parents=True, exist_ok=True)
    items = parse_nav()
    print(f"[scan] {len(items)} nav rows, "
          f"{sum(1 for _,_,p in items if p is not None)} markdown files")

    md_path = BUILD / "combined_nodecor.md"
    md_path.write_text(build_combined_md(items), encoding="utf-8")
    print(f"[md  ] {md_path}")

    DOCX.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        str(md_path),
        "--from=markdown+raw_html+fenced_divs+raw_tex+pipe_tables",
        "--to=docx",
        "--toc",
        "--toc-depth=3",
        "--metadata", "title=HMS Help - Combined Manual",
        "-o", str(DOCX),
    ]
    print(f"[run ] {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not DOCX.exists():
        print("[ERR ] pandoc failed:")
        print(r.stderr)
        return 1

    print(f"[docx] {DOCX} ({DOCX.stat().st_size/1024:.0f} KB)")
    print("[done]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
