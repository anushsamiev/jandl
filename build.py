#!/usr/bin/env python3
"""Assemble the static site: src/pages/*.html + src/partials -> dist/.

Each page starts with a small JSON front-matter block on the first lines,
delimited by a line containing only '---'.
"""
import json, re, shutil, datetime
from pathlib import Path

ROOT = Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"

# ---- Site-wide settings: edit here once, every page updates ----
SITE = {
    "site_url": "https://www.jlbailbonds.com",   # TODO: real domain
    "phone": "(318) 555-0199",                   # TODO: real phone number
    "tel": "+13185550199",                       # TODO: real phone number (E.164)
    "year": str(datetime.date.today().year),
}

def render(template: str, ctx: dict, slug: str) -> str:
    def active(m):
        return ' aria-current="page"' if m.group(1) == slug else ""
    template = re.sub(r"\{\{active:([a-z0-9-]+)\}\}", active, template)
    for k, v in ctx.items():
        template = template.replace("{{" + k + "}}", v)
    return template

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(SRC / "assets", DIST / "assets")
    head = (SRC / "partials/head.html").read_text()
    header = (SRC / "partials/header.html").read_text()
    footer = (SRC / "partials/footer.html").read_text()
    for page in sorted((SRC / "pages").glob("*.html")):
        raw = page.read_text()
        fm, body = raw.split("\n---\n", 1)
        meta = json.loads(fm)
        slug = page.stem
        ctx = {**SITE, **meta, "slug": "" if slug == "index" else slug + ".html"}
        html = render(head + header + body + footer, ctx, slug)
        (DIST / page.name).write_text(html)
        print("built", page.name)

if __name__ == "__main__":
    main()
