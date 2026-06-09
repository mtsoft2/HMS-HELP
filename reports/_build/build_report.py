"""
Build a single PDF of every documented module on the HMS Help site.

Pipeline:
  1. Parse mkdocs.yml to get the nav order.
  2. Walk every referenced .md file, prepend an H1 with the nav label.
  3. Prepend a cover page (cover.md) at the very top.
  4. Pandoc the whole thing into a styled HTML file with a TOC.
  5. Headless Chrome prints that HTML to a single PDF.

Outputs:
  E:\\Work\\HMS-HELP\\reports\\_build\\combined.md
  E:\\Work\\HMS-HELP\\reports\\_build\\combined.html
  E:\\Work\\HMS-HELP\\reports\\HMS-Help-Full.pdf
"""

from __future__ import annotations

import datetime as _dt
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT  = Path(r"E:/Work/HMS-HELP")
DOCS  = ROOT / "docs"
NAV   = ROOT / "mkdocs.yml"
OUT   = ROOT / "reports"
BUILD = OUT / "_build"
PDF   = OUT / "HMS-Help-Full.pdf"

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# --------------------------------------------------------------------------- #
#  1.  Parse mkdocs.yml nav into a flat ordered list of (depth, label, path)  #
# --------------------------------------------------------------------------- #
def parse_nav() -> list[tuple[int, str, Path | None]]:
    """Return [(indent_depth, label, md_path_or_None), …] in nav order."""
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
            break  # nav block ended

        stripped = raw.lstrip()
        if not stripped.startswith("-"):
            continue
        indent = (len(raw) - len(stripped)) // 2  # 2-space indents
        body = stripped[1:].strip()

        # `- Label: path` or `- Label:` (group)
        m = re.match(r"^([^:]+):\s*(.*)$", body)
        if not m:
            continue
        label, value = m.group(1).strip(), m.group(2).strip()
        if value:
            md = DOCS / value
            out.append((indent, label, md if md.exists() else None))
        else:
            out.append((indent, label, None))  # group header

    return out


# --------------------------------------------------------------------------- #
#  2.  Build the combined markdown                                            #
# --------------------------------------------------------------------------- #
def build_combined_md(items: list[tuple[int, str, Path | None]]) -> str:
    today = _dt.date.today().isoformat()

    cover = f"""---
title: "HMS Help — Combined Manual"
author: "MT Soft"
date: "{today}"
---

::: {{.cover-page}}

<div class="cover-brand">MT Soft</div>

# HMS Help

## Combined End-User &amp; Administrator Manual

<div class="cover-subtitle">Hospital Management System</div>

<div class="cover-meta">
Generated {today}<br/>
Source: <a href="https://mtsoft2.github.io/HMS-HELP/">https://mtsoft2.github.io/HMS-HELP/</a><br/>
Repository: <a href="https://github.com/mtsoft2/HMS-HELP">github.com/mtsoft2/HMS-HELP</a>
</div>

:::

<div class="page-break"></div>

# Table of Contents {{.toc-title}}

"""

    body_parts: list[str] = []
    # First-level (depth-0) labels become H1 chapter titles; deeper nav rows
    # are absorbed into the existing H1 inside the .md file.
    for depth, label, md in items:
        if depth == 0 and md is None:
            # top-level group, e.g. "Setup & Maintenance"
            body_parts.append(f'\n\n<div class="page-break"></div>\n\n# {label}\n\n')
            continue
        if md is None:
            continue
        try:
            content = md.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = md.read_text(encoding="utf-8", errors="replace")

        # Strip YAML front-matter so it isn't dumped as text.
        content = re.sub(r"^---\n.*?\n---\n", "", content, count=1, flags=re.S)

        # Rewrite relative image paths to absolute file:// so pandoc finds them.
        def _img(m):
            url = m.group(2)
            if re.match(r"^https?://", url):
                return m.group(0)
            abs_path = (md.parent / url).resolve()
            if abs_path.exists():
                return f"![{m.group(1)}]({abs_path.as_posix()})"
            return m.group(0)

        content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _img, content)

        # Strip MkDocs-Material caption directives  (/// caption … ///)
        # — pandoc renders them as raw text otherwise.
        content = re.sub(
            r"^/// caption\n(.*?)^///\s*$",
            lambda m: f"\n*{m.group(1).strip()}*\n",
            content,
            flags=re.S | re.M,
        )

        # Demote every heading by `depth` so the nav hierarchy survives.
        # depth 1 → demote by 1, depth 2 → demote by 2, etc.
        if depth > 0:
            def _demote(m, d=depth):
                hashes = m.group(1) + "#" * d
                # Don't go past h6.
                hashes = hashes[:6]
                return f"{hashes} {m.group(2)}"
            content = re.sub(r"^(#{1,6})\s+(.+)$", _demote, content, flags=re.M)

        body_parts.append(
            f'\n\n<div class="page-break"></div>\n\n{content}\n'
        )

    return cover + "\n".join(body_parts)


# --------------------------------------------------------------------------- #
#  3.  Stylesheet for the rendered HTML                                       #
# --------------------------------------------------------------------------- #
CSS = r"""
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body {
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  color: #1F2937;
}
h1, h2, h3, h4, h5, h6 { color: #1E3A8A; font-weight: 700; }
h1 { font-size: 22pt; margin-top: 0.4em; border-bottom: 2px solid #3949AB; padding-bottom: 6px; }
h2 { font-size: 16pt; margin-top: 1.5em; }
h3 { font-size: 13pt; margin-top: 1.4em; color: #2563EB; }
h4 { font-size: 11.5pt; margin-top: 1.2em; color: #334155; }
h5, h6 { font-size: 11pt; color: #475569; }
p  { margin: 0.4em 0 0.6em 0; }
ul, ol { margin: 0.4em 0 0.6em 1.4em; }
li { margin: 0.15em 0; }
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

/* Cover page */
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
  border-radius: 0;
}
.cover-page h1 {
  color: #fff;
  font-size: 44pt;
  border: 0;
  margin: 0.1em 0 0.2em 0;
}
.cover-page h2 {
  color: rgba(255,255,255,0.95);
  font-size: 22pt;
  margin: 0.4em 0;
}
.cover-brand {
  font-size: 14pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  opacity: 0.85;
  margin-bottom: 24px;
}
.cover-subtitle {
  font-size: 16pt;
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

/* Pandoc table-of-contents block */
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


# --------------------------------------------------------------------------- #
#  4.  Build pipeline                                                          #
# --------------------------------------------------------------------------- #
def main() -> int:
    BUILD.mkdir(parents=True, exist_ok=True)

    items = parse_nav()
    print(f"[scan] {len(items)} nav rows; "
          f"{sum(1 for _,_,p in items if p is not None)} markdown files")

    combined_md   = BUILD / "combined.md"
    combined_html = BUILD / "combined.html"
    css_file      = BUILD / "report.css"

    combined_md.write_text(build_combined_md(items), encoding="utf-8")
    css_file.write_text(CSS, encoding="utf-8")
    print(f"[md  ] {combined_md}")

    # Pandoc → HTML (single, self-contained, with TOC)
    cmd = [
        "pandoc",
        str(combined_md),
        "--from=gfm+raw_html+attributes+fenced_divs",
        "--to=html5",
        "--standalone",
        "--toc",
        "--toc-depth=3",
        "--metadata", "title=HMS Help — Combined Manual",
        "--css", str(css_file.as_posix()),
        "--embed-resources",
        "-o", str(combined_html),
    ]
    print(f"[run ] {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("[ERR ] pandoc failed:")
        print(r.stderr)
        return 1
    print(f"[html] {combined_html} ({combined_html.stat().st_size/1024:.0f} KB)")

    # Chrome headless → PDF
    PDF.parent.mkdir(parents=True, exist_ok=True)
    file_url = "file:///" + str(combined_html).replace("\\", "/")
    chrome_cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF}",
        "--print-to-pdf-no-header",
        "--virtual-time-budget=30000",
        file_url,
    ]
    print(f"[run ] chrome --headless --print-to-pdf …")
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
