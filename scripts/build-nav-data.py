#!/usr/bin/env python3
"""Read mkdocs.yml's nav and emit docs/assets/javascripts/nav-data.js.

The output is a small JS file that defines `window.HMS_NAV` — an array of
top-level sections, each with a label and a list of column groups, each
group being a label + list of {label, href} leaves.

The mega-menu.js consumer reads `window.HMS_NAV` and builds the dropdown
panels — independent of Material's runtime DOM lifting behaviour.
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML missing. Install with: pip install pyyaml\n")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "mkdocs.yml"
OUT = ROOT / "docs" / "assets" / "javascripts" / "nav-data.js"


def page_url(md_path: str) -> str:
    """Convert a docs/-relative .md path to the rendered URL."""
    p = md_path.replace("\\", "/")
    if p.endswith("/index.md"):
        return p[:-len("index.md")]
    if p.endswith(".md"):
        return p[:-len(".md")] + "/"
    return p


def walk(items):
    """Walk the nav tree → list of dicts {label, href?, groups?}.

    A leaf is {label, href}. A section is {label, groups: [{label, items: [...]}]}.
    """
    out = []
    if not isinstance(items, list):
        return out
    for it in items:
        if isinstance(it, str):
            # bare string = a path; label is missing — skip
            continue
        if isinstance(it, dict):
            for label, val in it.items():
                if isinstance(val, str):
                    out.append({"label": label, "href": page_url(val)})
                elif isinstance(val, list):
                    out.append({"label": label, "items": walk(val)})
    return out


def flatten_to_columns(node):
    """Turn one top-section's children into columns.

    Strategy:
    * If a child is a leaf → it becomes a single-item column with no header.
    * If a child is a sub-section → it becomes a column with the section label
      as header and its descendants as leaves.
    """
    cols = []
    for child in node.get("items", []):
        if "href" in child:
            cols.append({"label": None, "items": [child]})
        else:
            # collect all leaf descendants
            leaves = []
            stack = list(child.get("items", []))
            while stack:
                n = stack.pop(0)
                if "href" in n:
                    leaves.append(n)
                else:
                    stack[0:0] = n.get("items", [])
            cols.append({"label": child["label"], "items": leaves})
    return cols


def main():
    cfg_src = CFG.read_text(encoding="utf-8")
    # PyYAML chokes on Material's `!!python/name:` tags — strip the lines first.
    cfg_src = re.sub(r"^\s*emoji_index:.*$", "", cfg_src, flags=re.M)
    cfg_src = re.sub(r"^\s*emoji_generator:.*$", "", cfg_src, flags=re.M)
    cfg = yaml.safe_load(cfg_src)
    nav = cfg.get("nav") or []
    sections = walk(nav)

    out = []
    for s in sections:
        if "items" not in s:
            # top-level leaf (e.g. Home) — no dropdown
            out.append({"label": s["label"], "href": s.get("href"), "columns": []})
        else:
            out.append({"label": s["label"], "columns": flatten_to_columns(s)})

    js = "/* auto-generated from mkdocs.yml — do not edit by hand */\n"
    js += "window.HMS_NAV = " + json.dumps(out, indent=2, ensure_ascii=False) + ";\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(js, encoding="utf-8")
    print(f"wrote {OUT} ({len(out)} top-level sections)")


if __name__ == "__main__":
    main()
