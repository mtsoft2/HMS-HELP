"""
Build the 'HMS Release Update' PDF.

Differences vs build_report.py:
  * Title: 'HMS Release Update' (not 'HMS Help').
  * Excludes Human Resources, Payroll, and any 'Coming Soon' modules.
  * Strips every emoji + decorative icon marker.
  * Strips every horizontal rule (--- *** ___).
  * No CSS rulers anywhere (no border-bottom on H1, no <hr>).
  * Cover page kept; TOC kept.

Output:
  E:\\Work\\HMS-HELP\\reports\\HMS-Release-Update.pdf
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
PDF   = OUT / "HMS-Release-Update.pdf"

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Top-level nav labels to drop entirely (case-insensitive contains).
EXCLUDE_TOP = (
    "human resources",
    "payroll",
    "coming soon",
)

# Also drop the home page (its 'Coming Soon' card section and decorative
# hero gradient don't fit a release-update document).
EXCLUDE_PATHS = (
    "index.md",
)


# ---------- emoji + decorative-character ranges ---------- #
_EMOJI_RE = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "☀-➿"
    "←-⇿"
    "⌀-⏿"
    "①-⓿"
    "■-◿"
    "︀-️"
    "‍"
    "]+",
    flags=re.UNICODE,
)


# ---------- mkdocs.yml nav parser ---------- #
def parse_nav():
    lines = NAV.read_text(encoding="utf-8").splitlines()
    in_nav = False
    rows: list[tuple[int, str, Path | None]] = []
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
            rows.append((indent, label, md if md.exists() else None))
        else:
            rows.append((indent, label, None))
    return rows


# ---------- filter out excluded top-level groups ---------- #
def filter_nav(rows):
    """Drop every row whose top-level (depth-0) ancestor matches EXCLUDE_TOP."""
    out = []
    skipping = False
    for depth, label, md in rows:
        if depth == 0:
            skipping = any(needle in label.lower() for needle in EXCLUDE_TOP)
        if skipping:
            continue
        if md is not None:
            rel = md.relative_to(DOCS).as_posix()
            if any(rel == bad or rel.endswith("/" + bad) for bad in EXCLUDE_PATHS):
                continue
        out.append((depth, label, md))
    return out


# ---------- sanitisation ---------- #
def strip_decorations(text: str) -> str:
    text = _EMOJI_RE.sub("", text)
    text = re.sub(r":material-[a-z0-9-]+:", "", text)
    text = re.sub(r":octicons-[a-z0-9-]+:", "", text)
    text = re.sub(r":fontawesome-[a-z0-9-]+:", "", text)
    # Horizontal-rule lines (alone on a line)
    text = re.sub(r"^\s*[-*_]{3,}\s*$\n?", "", text, flags=re.M)
    # MkDocs attribute syntax {.css-class}
    text = re.sub(r"\s*\{[#.][^}]+\}\s*$", "", text, flags=re.M)
    # Collapse extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


# ---------- build combined markdown ---------- #
def build_md(items) -> str:
    today = _dt.date.today().isoformat()
    cover = f"""---
title: "HMS Release Update"
author: "MT Soft"
date: "{today}"
---

::: {{.cover-page}}

<div class="cover-brand">MT Soft</div>

# HMS Release Update

<div class="cover-subtitle">Hospital Management System</div>

<div class="cover-meta">
Generated {today}<br/>
Source: <a href="https://mtsoft2.github.io/HMS-HELP/">mtsoft2.github.io/HMS-HELP</a>
</div>

:::

<div class="page-break"></div>

# Table of Contents {{.toc-title}}

"""

    parts: list[str] = []
    for depth, label, md in items:
        if depth == 0 and md is None:
            parts.append(f'\n\n<div class="page-break"></div>\n\n# {label}\n\n')
            continue
        if md is None:
            continue
        try:
            content = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = md.read_text(encoding="utf-8", errors="replace")

        # Strip YAML front-matter
        content = re.sub(r"^---\n.*?\n---\n", "", content, count=1, flags=re.S)
        # Strip raw <style> blocks
        content = re.sub(r"<style[^>]*>.*?</style>", "", content,
                         flags=re.S | re.I)

        # Rewrite relative image paths to absolute
        def _img(m):
            url = m.group(2)
            if re.match(r"^https?://", url):
                return m.group(0)
            abs_path = (md.parent / url).resolve()
            if abs_path.exists():
                return f"![{m.group(1)}]({abs_path.as_posix()})"
            return m.group(0)
        content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _img, content)

        # MkDocs caption blocks
        content = re.sub(
            r"^/// caption\n(.*?)^///\s*$",
            lambda m: f"\n*{m.group(1).strip()}*\n",
            content,
            flags=re.S | re.M,
        )

        # Demote headings by nav depth
        if depth > 0:
            def _demote(m, d=depth):
                hashes = (m.group(1) + "#" * d)[:6]
                return f"{hashes} {m.group(2)}"
            content = re.sub(r"^(#{1,6})\s+(.+)$", _demote, content, flags=re.M)

        content = strip_decorations(content)
        parts.append(f'\n\n<div class="page-break"></div>\n\n{content}\n')

    return strip_decorations(cover + "\n".join(parts))


# ---------- stylesheet (NO rulers anywhere) ---------- #
CSS = r"""
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  color: #1F2937;
}
h1, h2, h3, h4, h5, h6 { color: #1E3A8A; font-weight: 700; border: 0; }
h1 { font-size: 22pt; margin-top: 0.4em; padding-bottom: 0; }
h2 { font-size: 16pt; margin-top: 1.5em; }
h3 { font-size: 13pt; margin-top: 1.4em; color: #2563EB; }
h4 { font-size: 11.5pt; margin-top: 1.2em; color: #334155; }
h5, h6 { font-size: 11pt; color: #475569; }
p  { margin: 0.4em 0 0.6em 0; }
ul, ol { margin: 0.4em 0 0.6em 1.4em; }
li { margin: 0.15em 0; }
hr { display: none; }
code {
  font-family: "Consolas", "Courier New", monospace;
  font-size: 9.5pt;
  background: #F1F5F9;
  padding: 1px 4px;
  border-radius: 3px;
}
pre {
  background: #F1F5F9;
  padding: 10px 12px;
  border-radius: 6px;
  font-size: 9.5pt;
  overflow-x: auto;
}
pre code { background: transparent; padding: 0; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.6em 0 1em 0;
  font-size: 10pt;
}
th, td {
  border: 1px solid #CBD5E1;
  padding: 6px 9px;
  text-align: left;
  vertical-align: top;
}
th { background: #E0E7FF; color: #1E3A8A; font-weight: 600; }
img { max-width: 95%; height: auto; display: block; margin: 8px auto; }
blockquote {
  margin: 0.5em 0;
  padding: 6px 14px;
  border-left: 4px solid #3949AB;
  background: #EEF2FF;
  color: #1E3A8A;
}
a { color: #2563EB; text-decoration: none; }
em { color: #475569; }

.page-break { page-break-before: always; }

/* Cover */
.cover-page {
  page-break-after: always;
  height: 92vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: linear-gradient(135deg, #3949AB 0%, #1E88E5 100%);
  color: #fff;
  padding: 60px 40px;
  margin: -18mm -16mm;
}
.cover-page h1 {
  color: #fff;
  font-size: 48pt;
  margin: 0.1em 0 0.2em 0;
}
.cover-brand {
  font-size: 14pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  opacity: 0.85;
  margin-bottom: 24px;
}
.cover-subtitle {
  font-size: 18pt;
  font-style: italic;
  margin: 0.8em 0 2.2em 0;
  opacity: 0.95;
}
.cover-meta {
  margin-top: 3em;
  font-size: 11pt;
  line-height: 1.6;
  opacity: 0.92;
}
.cover-meta a { color: #fff; text-decoration: underline; }

.toc-title { page-break-after: avoid; }

#TOC {
  font-size: 10.5pt;
  border: 1px solid #CBD5E1;
  background: #F8FAFC;
  padding: 14px 20px 16px 30px;
  border-radius: 8px;
  margin: 6px 0 30px 0;
}
#TOC ul { list-style: none; padding-left: 1em; }
#TOC > ul { padding-left: 0; }
#TOC li { margin: 3px 0; }
#TOC a { color: #1E3A8A; }
"""


def main() -> int:
    BUILD.mkdir(parents=True, exist_ok=True)
    rows = parse_nav()
    items = filter_nav(rows)
    print(f"[scan] nav rows total={len(rows)} kept={len(items)} "
          f"md_files={sum(1 for _,_,p in items if p)}")

    md = BUILD / "release_update.md"
    html = BUILD / "release_update.html"
    css = BUILD / "release_update.css"

    md.write_text(build_md(items), encoding="utf-8")
    css.write_text(CSS, encoding="utf-8")
    print(f"[md  ] {md}")

    cmd = [
        "pandoc",
        str(md),
        "--from=markdown+raw_html+fenced_divs+pipe_tables",
        "--to=html5",
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--metadata", "title=HMS Release Update",
        "--css", str(css.as_posix()),
        "--embed-resources",
        "-o", str(html),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("[ERR ] pandoc failed:")
        print(r.stderr)
        return 1
    print(f"[html] {html} ({html.stat().st_size/1024:.0f} KB)")

    PDF.parent.mkdir(parents=True, exist_ok=True)
    chrome_cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={PDF}",
        "--print-to-pdf-no-header",
        "--no-pdf-header-footer",
        "--virtual-time-budget=30000",
        "file:///" + str(html).replace("\\", "/"),
    ]
    r = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if r.returncode != 0 or not PDF.exists():
        print("[ERR ] chrome failed:")
        print(r.stderr)
        return 2
    print(f"[pdf ] {PDF} ({PDF.stat().st_size/1024:.0f} KB)")
    print("[done]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
