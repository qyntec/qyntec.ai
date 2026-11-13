#!/usr/bin/env python3
"""Check titles, meta tags, JSON-LD, and sitemap coverage for qyntec.ai."""

from __future__ import annotations

import json
import struct
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    {
        "file": "index.html",
        "canonical": "https://qyntec.ai/",
        "image": "assets/og/home.png",
        "software": True,
    },
    {
        "file": "contact.html",
        "canonical": "https://qyntec.ai/contact.html",
        "image": "assets/og/contact.png",
        "software": False,
    },
    {
        "file": "privacy.html",
        "canonical": "https://qyntec.ai/privacy.html",
        "image": "assets/og/privacy.png",
        "software": False,
    },
    {
        "file": "terms.html",
        "canonical": "https://qyntec.ai/terms.html",
        "image": "assets/og/terms.png",
        "software": False,
    },
    {
        "file": "thank-you.html",
        "canonical": "https://qyntec.ai/thank-you.html",
        "image": "assets/og/thank-you.png",
        "software": False,
    },
]

AI_CRAWLERS = [
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-User",
    "Claude-SearchBot",
    "PerplexityBot",
    "Perplexity-User",
    "Google-Extended",
    "Applebot-Extended",
    "CCBot",
]

OG_REQUIRED = [
    "og:title",
    "og:description",
    "og:url",
    "og:type",
    "og:site_name",
    "og:image",
    "og:image:alt",
]

FORBIDDEN = {
    "\u2014": "em dash",
    "\u2013": "en dash",
    "\u2192": "arrow",
    "\u2190": "arrow",
    "\u21d2": "arrow",
    "\u2794": "arrow",
}

FAVICONS = {
    "favicon.ico": None,
    "favicon.svg": None,
    "favicon-16x16.png": (16, 16),
    "favicon-32x32.png": (32, 32),
    "apple-touch-icon.png": (180, 180),
    "android-chrome-192x192.png": (192, 192),
    "android-chrome-512x512.png": (512, 512),
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = []
        self.in_title = False
        self.h1 = 0
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.svgs: list[dict[str, str]] = []
        self.json_ld: list[str] = []
        self._in_ld = False
        self._ld_buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1 += 1
        elif tag == "meta":
            self.metas.append(data)
        elif tag == "link":
            self.links.append(data)
        elif tag == "img":
            self.images.append(data)
        elif tag == "svg":
            self.svgs.append(data)
        elif tag == "script" and data.get("type") == "application/ld+json":
            self._in_ld = True
            self._ld_buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self._in_ld:
            self.json_ld.append("".join(self._ld_buf))
            self._in_ld = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title.append(data)
        elif self._in_ld:
            self._ld_buf.append(data)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError(f"{path.name} is not a PNG")
    return struct.unpack(">II", data[16:24])


def ico_sizes(path: Path) -> list[tuple[int, int]]:
    data = path.read_bytes()
    reserved, kind, count = struct.unpack_from("<HHH", data, 0)
    if reserved != 0 or kind != 1:
        raise ValueError("favicon.ico is not an ICO")
    sizes = []
    for index in range(count):
        width, height = struct.unpack_from("<BB", data, 6 + 16 * index)
        sizes.append((width or 256, height or 256))
    return sizes


def meta_map(parser: PageParser) -> dict[str, str]:
    found: dict[str, str] = {}
    for meta in parser.metas:
        key = meta.get("name") or meta.get("property")
        if key:
            found[key] = meta.get("content", "")
    return found


def graph_types(payload: object) -> list[dict]:
    nodes: list[dict] = []
    if isinstance(payload, list):
        for item in payload:
            nodes.extend(graph_types(item))
        return nodes
    if not isinstance(payload, dict):
        return nodes
    if "@graph" in payload:
        nodes.extend(graph_types(payload["@graph"]))
    if "@type" in payload:
        nodes.append(payload)
    return nodes


def forbidden_hits(text: str) -> list[str]:
    hits = []
    for char, name in FORBIDDEN.items():
        if char in text:
            hits.append(name)
    if "->" in text:
        hits.append("arrow")
    return hits


def check_pages(errors: list[str], notes: list[str]) -> None:
    titles: dict[str, str] = {}
    for page in PAGES:
        path = ROOT / page["file"]
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        title = " ".join("".join(parser.title).split())
        metas = meta_map(parser)
        description = metas.get("description", "")
        label = page["file"]

        if not title:
            errors.append(f"{label}: missing title")
        elif len(title) > 60:
            errors.append(f"{label}: title is {len(title)} characters (max 60): {title}")
        elif title in titles.values():
            errors.append(f"{label}: title is not unique: {title}")
        titles[label] = title

        if not 150 <= len(description) <= 160:
            errors.append(
                f"{label}: meta description is {len(description)} characters (need 150-160)"
            )

        canonicals = [
            link.get("href", "")
            for link in parser.links
            if link.get("rel") == "canonical"
        ]
        if canonicals != [page["canonical"]]:
            errors.append(f"{label}: canonical is {canonicals}, expected {page['canonical']}")

        for key in OG_REQUIRED:
            if not metas.get(key):
                errors.append(f"{label}: missing {key}")
        if metas.get("og:type") != "website":
            errors.append(f"{label}: og:type is {metas.get('og:type')!r}")
        if metas.get("og:site_name") != "Qyntec.ai":
            errors.append(f"{label}: og:site_name is {metas.get('og:site_name')!r}")
        if metas.get("og:url") != page["canonical"]:
            errors.append(f"{label}: og:url does not match canonical")
        if metas.get("og:title") != title:
            errors.append(f"{label}: og:title does not match the document title")
        if metas.get("og:description") != description:
            errors.append(f"{label}: og:description does not match meta description")
        image_url = f"https://qyntec.ai/{page['image']}"
        if metas.get("og:image") != image_url:
            errors.append(f"{label}: og:image is {metas.get('og:image')!r}")
        if metas.get("og:image:width") != "1200" or metas.get("og:image:height") != "630":
            errors.append(f"{label}: og image dimensions are not 1200x630")
        if metas.get("twitter:card") != "summary_large_image":
            errors.append(f"{label}: twitter:card is {metas.get('twitter:card')!r}")
        for key in ("twitter:title", "twitter:description", "twitter:image"):
            if not metas.get(key):
                errors.append(f"{label}: missing {key}")
        if metas.get("twitter:title") != title:
            errors.append(f"{label}: twitter:title does not match the document title")
        if metas.get("twitter:description") != description:
            errors.append(f"{label}: twitter:description does not match meta description")
        if metas.get("twitter:image") != image_url:
            errors.append(f"{label}: twitter:image does not match og:image")
        if not metas.get("twitter:image:alt"):
            errors.append(f"{label}: missing twitter:image:alt")
        robots = metas.get("robots", "")
        if "noindex" in robots:
            errors.append(f"{label}: robots meta sets noindex")

        image_path = ROOT / page["image"]
        if not image_path.is_file():
            errors.append(f"{label}: missing share image {page['image']}")
        else:
            size = png_size(image_path)
            if size != (1200, 630):
                errors.append(f"{label}: {page['image']} is {size[0]}x{size[1]}")

        if parser.h1 != 1:
            errors.append(f"{label}: found {parser.h1} h1 elements")
        for image in parser.images:
            alt = image.get("alt", "")
            if "alt" not in image or not alt.strip():
                errors.append(f"{label}: img is missing alt text ({image.get('src', '')})")
        if not any(svg.get("aria-label", "").strip() for svg in parser.svgs):
            errors.append(f"{label}: no svg has an accessible name")
        for svg in parser.svgs:
            named = bool(svg.get("aria-label", "").strip())
            hidden = svg.get("aria-hidden") == "true"
            if named == hidden:
                errors.append(f"{label}: svg needs aria-label or aria-hidden, not both or neither")

        for href in (
            "/favicon.ico",
            "/favicon.svg",
            "/favicon-16x16.png",
            "/favicon-32x32.png",
            "/apple-touch-icon.png",
            "/site.webmanifest",
        ):
            if not any(link.get("href") == href for link in parser.links):
                errors.append(f"{label}: missing link {href}")

        if len(parser.json_ld) != 1:
            errors.append(f"{label}: expected one JSON-LD script, found {len(parser.json_ld)}")
            continue
        try:
            payload = json.loads(parser.json_ld[0])
        except json.JSONDecodeError as exc:
            errors.append(f"{label}: JSON-LD did not parse ({exc})")
            continue
        nodes = graph_types(payload)
        types = [node.get("@type") for node in nodes]
        if "Organization" not in types or "WebSite" not in types:
            errors.append(f"{label}: JSON-LD types are {types}")
        has_software = "SoftwareApplication" in types
        if has_software != page["software"]:
            errors.append(
                f"{label}: SoftwareApplication present={has_software}, expected={page['software']}"
            )
        blob = json.dumps(payload)
        if "HIPAA" in blob or "HITECH" in blob:
            errors.append(f"{label}: JSON-LD includes a compliance claim")
        for node in nodes:
            if node.get("@type") == "Organization":
                if node.get("name") != "Qyntec.ai" or node.get("url") != "https://qyntec.ai/":
                    errors.append(f"{label}: Organization name or url is wrong")
                same = node.get("sameAs") or []
                if "https://www.linkedin.com/company/qyntec" not in same:
                    errors.append(f"{label}: Organization sameAs is missing LinkedIn")
            if node.get("@type") == "WebSite":
                if node.get("url") != "https://qyntec.ai/":
                    errors.append(f"{label}: WebSite url is wrong")
            if node.get("@type") == "SoftwareApplication":
                if node.get("url") != "https://qyntec.ai/":
                    errors.append(f"{label}: SoftwareApplication url is wrong")

        copy_bits = [title, description, *[metas.get(key, "") for key in OG_REQUIRED]]
        copy_bits.extend(metas.get(key, "") for key in ("twitter:title", "twitter:description", "twitter:image:alt"))
        copy_bits.append(parser.json_ld[0] if parser.json_ld else "")
        hits = forbidden_hits("\n".join(copy_bits))
        if hits:
            errors.append(f"{label}: copy contains {', '.join(sorted(set(hits)))}")

        notes.append(
            f"{label}: title {len(title)} chars, description {len(description)} chars, h1 {parser.h1}, json-ld {', '.join(str(t) for t in types)}"
        )


def check_robots(errors: list[str]) -> None:
    text = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "Sitemap: https://qyntec.ai/sitemap.xml" not in text:
        errors.append("robots.txt does not reference the sitemap")
    blocks = []
    current: list[str] = []
    for line in text.splitlines():
        if not line.strip():
            if current:
                blocks.append(current)
                current = []
            continue
        current.append(line.strip())
    if current:
        blocks.append(current)
    allowed = set()
    for block in blocks:
        agents = [line.split(":", 1)[1].strip() for line in block if line.lower().startswith("user-agent:")]
        allows = any(line.lower() == "allow: /" for line in block)
        if allows:
            allowed.update(agents)
    missing = [bot for bot in AI_CRAWLERS if bot not in allowed]
    if missing:
        errors.append("robots.txt does not allow: " + ", ".join(missing))
    if "*" not in allowed:
        errors.append("robots.txt does not allow search engines with User-agent: *")


def check_sitemap(errors: list[str]) -> None:
    tree = ET.parse(ROOT / "sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [node.text.strip() for node in tree.findall("sm:url/sm:loc", ns) if node.text]
    expected = [page["canonical"] for page in PAGES]
    if locs != expected:
        errors.append(f"sitemap locs {locs} do not match page canonicals {expected}")


def check_llms(errors: list[str]) -> None:
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    full = (ROOT / "llms-full.txt").read_text(encoding="utf-8")
    if not llms.startswith("# Qyntec.ai\n"):
        errors.append("llms.txt must start with the site H1")
    if "\n> " not in llms:
        errors.append("llms.txt is missing the summary blockquote")
    for page in PAGES:
        if page["canonical"] not in llms:
            errors.append(f"llms.txt is missing {page['canonical']}")
        if page["canonical"] not in full:
            errors.append(f"llms-full.txt is missing {page['canonical']}")
    if "HIPAA" in llms or "HITECH" in llms:
        errors.append("llms.txt includes a compliance claim")
    for name, text in (("llms.txt", llms), ("llms-full.txt", full)):
        hits = forbidden_hits(text)
        if hits:
            errors.append(f"{name} contains {', '.join(sorted(set(hits)))}")
    if len(full) < 3000:
        errors.append("llms-full.txt does not include the page copy")


def check_favicons(errors: list[str]) -> None:
    for name, size in FAVICONS.items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing {name}")
            continue
        if name.endswith(".png") and size and png_size(path) != size:
            errors.append(f"{name} is {png_size(path)}, expected {size}")
    ico = ico_sizes(ROOT / "favicon.ico")
    if ico != [(16, 16), (32, 32), (48, 48)]:
        errors.append(f"favicon.ico sizes are {ico}")
    manifest = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
    icon_srcs = {icon.get("src") for icon in manifest.get("icons", [])}
    for src in ("/android-chrome-192x192.png", "/android-chrome-512x512.png", "/apple-touch-icon.png"):
        if src not in icon_srcs:
            errors.append(f"site.webmanifest is missing {src}")


def main() -> int:
    errors: list[str] = []
    notes: list[str] = []
    check_pages(errors, notes)
    check_robots(errors)
    check_sitemap(errors)
    check_llms(errors)
    check_favicons(errors)

    print("Qyntec.ai SEO check")
    print("pages: " + ", ".join(page["file"] for page in PAGES))
    for note in notes:
        print(note)
    print(f"sitemap urls: {len(PAGES)}")
    print("robots.txt allows search engines and " + ", ".join(AI_CRAWLERS))
    print("llms.txt and llms-full.txt present")
    if errors:
        print(f"RESULT: FAIL ({len(errors)})")
        for error in errors:
            print(f"- {error}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
