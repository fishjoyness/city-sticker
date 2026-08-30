#!/usr/bin/env python3
"""Build a city sticker showcase from a city manifest."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simhei.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    raise FileNotFoundError("No supported Chinese font found")


def build(manifest_path: Path, output: Path, columns: int) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    landmarks = manifest["landmarks"]
    rows = math.ceil(len(landmarks) / columns)
    card = 330
    gap = 24
    left = 56
    top = 130
    width = left * 2 + columns * card + (columns - 1) * gap
    height = top + rows * card + (rows - 1) * gap + 56
    canvas = Image.new("RGB", (width, height), "#F3EFE8")
    draw = ImageDraw.Draw(canvas)
    draw.text((left, 38), f"{manifest['cityChinese']} · 15 LANDMARK STICKERS", fill="#282621", font=font(42, True))

    for index, landmark in enumerate(landmarks):
        row, column = divmod(index, columns)
        x = left + column * (card + gap)
        y = top + row * (card + gap)
        draw.rounded_rectangle((x, y, x + card, y + card), radius=26, fill="#FFFEFB", outline="#D9D1C7", width=2)
        image_name = landmark.get("transparent", f"{landmark['slug']}_transparent.png")
        image_path = manifest_path.parent / image_name
        sticker = Image.open(image_path).convert("RGBA")
        sticker.thumbnail((card - 24, card - 24), Image.Resampling.LANCZOS)
        canvas.paste(sticker, (x + (card - sticker.width) // 2, y + (card - sticker.height) // 2), sticker)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, "PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--columns", type=int, default=5)
    args = parser.parse_args()
    if args.columns < 1:
        parser.error("--columns must be positive")
    build(args.manifest, args.output, args.columns)


if __name__ == "__main__":
    main()
