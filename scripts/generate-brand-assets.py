#!/usr/bin/env python3
"""Build the favicon set and 1200x630 share images from the Qyntec logo.

Uses the heart mark in assets/logo-icon-only.svg, the site background
(#0a0a0a), the emerald-to-cyan brand gradient, and Inter.
"""

from __future__ import annotations

import io
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
LOGO_SVG = ROOT / "assets" / "logo-icon-only.svg"
OG_DIR = ROOT / "assets" / "og"

FONT_BOLD = "/usr/share/fonts/truetype/macos/Inter-Bold.ttf"
FONT_SEMIBOLD = "/usr/share/fonts/truetype/macos/Inter-SemiBold.ttf"
FONT_MEDIUM = "/usr/share/fonts/truetype/macos/Inter-Medium.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"

BG = (10, 10, 10)
EMERALD = (16, 185, 129)
CYAN = (6, 182, 212)
DEEP = (5, 150, 105)
WHITE = (255, 255, 255)
MUTED = (192, 192, 192)
DIM = (160, 160, 160)

WIDTH = 1200
HEIGHT = 630

CARDS = [
    {
        "file": "home.png",
        "eyebrow": "Coming soon",
        "title": "The healthcare platform clinicians actually want",
        "subtitle": "A unified, AI-powered platform with zero legacy constraints.",
    },
    {
        "file": "contact.png",
        "eyebrow": "Contact",
        "title": "Get in touch",
        "subtitle": "Questions, partnerships, and early access.",
    },
    {
        "file": "privacy.png",
        "eyebrow": "Privacy",
        "title": "Privacy Policy",
        "subtitle": "How we collect, use, and safeguard information.",
    },
    {
        "file": "terms.png",
        "eyebrow": "Terms",
        "title": "Terms of Service",
        "subtitle": "Terms for the Qyntec.ai website and services.",
    },
    {
        "file": "thank-you.png",
        "eyebrow": "Early access",
        "title": "You're on the list",
        "subtitle": "We will keep you updated and reach out before launch.",
    },
]


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def logo_svg() -> str:
    """Rasterize the mark with the gradient the logo file defines.

    The source gradient uses user-space coordinates but omits
    gradientUnits, so a default objectBoundingBox paint collapses to the
    first stop. userSpaceOnUse keeps the emerald-to-cyan fill. The stroke
    follows that same gradient, matching the inline logo on the pages.
    """
    svg = LOGO_SVG.read_text(encoding="utf-8")
    svg = svg.replace(
        '<linearGradient id="heartGradient"',
        '<linearGradient id="heartGradient" gradientUnits="userSpaceOnUse"',
        1,
    )
    svg = svg.replace('stroke="#10b981"', 'stroke="url(#heartGradient)"', 1)
    return svg


def render_logo(size: int) -> Image.Image:
    png = cairosvg.svg2png(
        bytestring=logo_svg().encode("utf-8"),
        output_width=size,
        output_height=size,
    )
    return Image.open(io.BytesIO(png)).convert("RGBA")


def new_canvas() -> Image.Image:
    return Image.new("RGBA", (WIDTH, HEIGHT), BG + (255,))


def add_orb(base: Image.Image, center: tuple[int, int], radius: int, color: tuple[int, int, int], alpha: int, blur: int) -> Image.Image:
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x, y = center
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    return Image.alpha_composite(base, layer)


def horizontal_gradient(size: tuple[int, int], left: tuple[int, int, int], right: tuple[int, int, int]) -> Image.Image:
    width, height = size
    gradient = Image.new("RGBA", size)
    pixels = gradient.load()
    for x in range(width):
        t = x / max(width - 1, 1)
        color = tuple(int(left[i] + (right[i] - left[i]) * t) for i in range(3)) + (255,)
        for y in range(height):
            pixels[x, y] = color
    return gradient


def wrap_text(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=face) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_title(draw: ImageDraw.ImageDraw, text: str, max_width: int) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(58, 36, -2):
        face = font(FONT_BOLD, size)
        lines = wrap_text(draw, text, face, max_width)
        if len(lines) <= 3 and all(draw.textlength(line, font=face) <= max_width for line in lines):
            return face, lines
    face = font(FONT_BOLD, 36)
    return face, wrap_text(draw, text, face, max_width)


def draw_card(spec: dict) -> Image.Image:
    canvas = new_canvas()
    canvas = add_orb(canvas, (1040, -30), 340, EMERALD, 80, 50)
    canvas = add_orb(canvas, (40, 680), 300, CYAN, 70, 46)
    canvas = add_orb(canvas, (620, 300), 180, DEEP, 40, 36)

    logo = render_logo(300)
    logo_x = 78
    logo_y = (HEIGHT - 300) // 2 - 16
    canvas.alpha_composite(logo, (logo_x, logo_y))

    draw = ImageDraw.Draw(canvas)
    text_x = 430
    text_width = 700
    title_font, title_lines = fit_title(draw, spec["title"], text_width)
    eyebrow_font = font(FONT_SEMIBOLD, 22)
    subtitle_font = font(FONT_REGULAR, 28)
    subtitle_lines = wrap_text(draw, spec["subtitle"], subtitle_font, text_width)

    title_size = title_font.size
    title_gap = title_size + 10
    subtitle_gap = 38
    block_height = (
        22
        + 22
        + title_gap * len(title_lines)
        + 16
        + subtitle_gap * len(subtitle_lines)
    )
    # Keep the copy in the upper-middle, clear of the footer band.
    y = max(120, (HEIGHT - 110 - block_height) // 2)

    draw.text((text_x, y), spec["eyebrow"], font=eyebrow_font, fill=EMERALD)
    y += 22 + 18
    for line in title_lines:
        draw.text((text_x, y), line, font=title_font, fill=WHITE)
        y += title_gap
    y += 8
    for line in subtitle_lines:
        draw.text((text_x, y), line, font=subtitle_font, fill=MUTED)
        y += subtitle_gap

    bar = horizontal_gradient((WIDTH, 8), EMERALD, CYAN)
    canvas.alpha_composite(bar, (0, HEIGHT - 8))

    footer_y = HEIGHT - 78
    mark = render_logo(44)
    canvas.alpha_composite(mark, (72, footer_y - 6))
    brand_font = font(FONT_BOLD, 26)
    tag_font = font(FONT_REGULAR, 20)
    draw = ImageDraw.Draw(canvas)
    draw.text((128, footer_y), "Qyntec.ai", font=brand_font, fill=WHITE)
    tagline = "Re-architecting Healthcare, One Record at a Time."
    tag_width = draw.textlength(tagline, font=tag_font)
    draw.text((WIDTH - 64 - tag_width, footer_y + 4), tagline, font=tag_font, fill=DIM)
    return canvas.convert("RGB")


def save_png(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG", optimize=True)


def build_favicons() -> None:
    for size, name in ((16, "favicon-16x16.png"), (32, "favicon-32x32.png")):
        save_png(render_logo(size), ROOT / name)

    ico_images = [render_logo(size) for size in (16, 32, 48)]
    ico_images[-1].save(
        ROOT / "favicon.ico",
        format="ICO",
        sizes=[(image.width, image.height) for image in ico_images],
        append_images=ico_images[:-1],
    )

    for size, name in (
        (180, "apple-touch-icon.png"),
        (192, "android-chrome-192x192.png"),
        (512, "android-chrome-512x512.png"),
    ):
        tile = Image.new("RGB", (size, size), BG)
        logo_size = int(size * 0.68)
        logo = render_logo(logo_size)
        offset = (size - logo_size) // 2
        tile.paste(logo, (offset, offset), logo)
        save_png(tile, ROOT / name)

    (ROOT / "favicon.svg").write_text(logo_svg(), encoding="utf-8")


def build_cards() -> None:
    OG_DIR.mkdir(parents=True, exist_ok=True)
    for spec in CARDS:
        card = draw_card(spec)
        if card.size != (WIDTH, HEIGHT):
            raise SystemExit(f"{spec['file']} is {card.size}, expected {(WIDTH, HEIGHT)}")
        save_png(card, OG_DIR / spec["file"])
        print(f"wrote assets/og/{spec['file']}")


def main() -> None:
    build_favicons()
    print("wrote favicon set")
    build_cards()


if __name__ == "__main__":
    main()
