#!/usr/bin/env python3
"""Build normalized transparent landmark stickers and the README showcase."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


CANVAS = 1024
ART_BOX = (790, 600)
ART_TOP = 105
LABEL_TOP = 770
LABEL_HEIGHT = 112
PREVIEW_BG = "#FFFFFF"


def alpha_crop(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    bounds = rgba.getchannel("A").getbbox()
    if not bounds:
        raise ValueError("input image has no visible alpha content")
    return rgba.crop(bounds)


def fit(image: Image.Image, max_width: int, max_height: int) -> Image.Image:
    ratio = min(max_width / image.width, max_height / image.height)
    size = (max(1, round(image.width * ratio)), max(1, round(image.height * ratio)))
    return image.resize(size, Image.Resampling.LANCZOS)


def font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("C:/Windows/Fonts/simsun.ttc"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    raise FileNotFoundError("No Chinese font found in the standard Windows font directory")


def build_asset(source: Path, name: str, transparent: Path, preview: Path) -> None:
    art = fit(alpha_crop(Image.open(source)), *ART_BOX)
    canvas = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))

    art_x = (CANVAS - art.width) // 2
    art_y = ART_TOP + (ART_BOX[1] - art.height) // 2
    canvas.alpha_composite(art, (art_x, art_y))

    draw = ImageDraw.Draw(canvas)
    label_font = font(58)
    text_box = draw.textbbox((0, 0), name, font=label_font)
    text_width = text_box[2] - text_box[0]
    label_width = max(280, text_width + 104)
    label_left = (CANVAS - label_width) // 2
    label_right = label_left + label_width
    label_bottom = LABEL_TOP + LABEL_HEIGHT

    shadow_box = (label_left + 6, LABEL_TOP + 8, label_right + 6, label_bottom + 8)
    draw.rounded_rectangle(shadow_box, radius=34, fill=(49, 44, 37, 26))
    draw.rounded_rectangle(
        (label_left, LABEL_TOP, label_right, label_bottom),
        radius=34,
        fill=(255, 253, 247, 255),
        outline=(45, 43, 39, 255),
        width=5,
    )
    text_y = LABEL_TOP + (LABEL_HEIGHT - (text_box[3] - text_box[1])) // 2 - text_box[1]
    draw.text(((CANVAS - text_width) // 2, text_y), name, font=label_font, fill=(39, 38, 35, 255))

    transparent.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(transparent, "PNG", optimize=True)

    white = Image.new("RGB", (CANVAS, CANVAS), PREVIEW_BG)
    white.paste(canvas, mask=canvas.getchannel("A"))
    preview.parent.mkdir(parents=True, exist_ok=True)
    white.save(preview, "PNG", optimize=True)


def build_showcase(inputs: list[Path], output: Path) -> None:
    if len(inputs) != 4:
        raise ValueError("showcase requires exactly four sticker assets")

    width, height = 1800, 1800
    showcase = Image.new("RGB", (width, height), PREVIEW_BG)
    draw = ImageDraw.Draw(showcase)
    title_font = font(70)
    draw.text((90, 68), "南京景点贴纸", font=title_font, fill=(39, 38, 35))

    card_size = 760
    positions = [(100, 190), (940, 190), (100, 1010), (940, 1010)]
    for source, (x, y) in zip(inputs, positions, strict=True):
        card = Image.new("RGB", (card_size, card_size), "#FCFBF8")
        card_draw = ImageDraw.Draw(card)
        card_draw.rounded_rectangle(
            (1, 1, card_size - 2, card_size - 2),
            radius=36,
            outline=(226, 223, 215),
            width=3,
        )
        sticker = Image.open(source).convert("RGBA").resize((700, 700), Image.Resampling.LANCZOS)
        card.paste(sticker, (30, 30), sticker)
        showcase.paste(card, (x, y))

    output.parent.mkdir(parents=True, exist_ok=True)
    showcase.save(output, "PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    asset = sub.add_parser("asset")
    asset.add_argument("--source", type=Path, required=True)
    asset.add_argument("--name", required=True)
    asset.add_argument("--transparent", type=Path, required=True)
    asset.add_argument("--preview", type=Path, required=True)

    showcase = sub.add_parser("showcase")
    showcase.add_argument("--inputs", type=Path, nargs=4, required=True)
    showcase.add_argument("--output", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "asset":
        build_asset(args.source, args.name, args.transparent, args.preview)
    else:
        build_showcase(args.inputs, args.output)


if __name__ == "__main__":
    main()
