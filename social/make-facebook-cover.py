#!/usr/bin/env python3
"""Rebuild the Facebook cover (851x315).

Layout, left to right: the beet mandolin over offbeet.ca in beet crimson,
then the band cutout with the Offbeet wordmark in black behind it.
Everything meaningful sits inside Facebook's 640px mobile safe area
(x 105-745). Run from the repo root: python3 social/make-facebook-cover.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 851, 315
BEET = (169, 30, 79)

cover = Image.new("RGB", (W, H), "white")

# --- wordmark in black, behind the band ---
word = Image.open("assets/wordmark.png")
w_w = 500
word = word.resize((w_w, round(word.height * w_w / word.width)), Image.LANCZOS)
cover.paste(word, (320, 34), word)

# --- band cutout, bottom-cropped by the canvas ---
band = Image.open("social/band-cutout.png")
band = band.crop(band.getbbox())
b_w = 438
band = band.resize((b_w, round(band.height * b_w / band.width)), Image.LANCZOS)
cover.paste(band, (297, 99), band)

# --- mandolin ---
mando = Image.open("assets/beet-guitar.png")
m_h = 213
mando = mando.resize((round(mando.width * m_h / mando.height), m_h), Image.LANCZOS)
mando_x = 203 - mando.width // 2
cover.paste(mando, (mando_x, 24), mando)

# --- offbeet.ca under the mandolin ---
draw = ImageDraw.Draw(cover)
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 24)
label = "offbeet.ca"
tw = draw.textbbox((0, 0), label, font=font)[2]
draw.text((203 - tw // 2, 262), label, font=font, fill=BEET)

cover.save("social/facebook-cover.png")
cover.save("social/facebook-cover.jpg", quality=88, optimize=True)
print("wrote social/facebook-cover.png and .jpg")
