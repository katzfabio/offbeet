#!/usr/bin/env python3
"""Rebuild the Facebook EVENT cover (1920x1005, 1.91:1).

Not the same image as the Page cover (851x315) -- Facebook crops an event
photo tighter than the feed preview suggests, chopping the sides. So this
one is composed on the centre line: the site's mandolin+wordmark lockup on
top, the band underneath, everything inside a 1.25:1 core box (x 332-1588)
that survives even the tightest crop Facebook applies.

Run from the repo root: python3 social/make-facebook-event.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1005
BEET = (169, 30, 79)
CX = W // 2

cover = Image.new("RGB", (W, H), "white")

# --- lockup: mandolin beside the wordmark, centred (mirrors the site header) ---
mando = Image.open("assets/beet-guitar.png")
m_h = 200
mando = mando.resize((round(mando.width * m_h / mando.height), m_h), Image.LANCZOS)

word = Image.open("assets/wordmark.png")
w_w = 560
word = word.resize((w_w, round(word.height * w_w / word.width)), Image.LANCZOS)

gap = 26
lock_w = mando.width + gap + word.width
lock_x = CX - lock_w // 2
lock_y = 34
cover.paste(mando, (lock_x, lock_y), mando)
word_y = lock_y + (m_h - word.height) // 2
cover.paste(word, (lock_x + mando.width + gap, word_y), word)

# --- band cutout, centred, bottom-cropped by the canvas ---
band = Image.open("social/band-cutout.png")
band = band.crop(band.getbbox())
b_w = 1330
band = band.resize((b_w, round(band.height * b_w / band.width)), Image.LANCZOS)
cover.paste(band, (CX - b_w // 2, H - band.height), band)

# --- offbeet.ca between the lockup and the band ---
draw = ImageDraw.Draw(cover)
font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 34)
label = "offbeet.ca"
tw = draw.textbbox((0, 0), label, font=font)[2]
draw.text((CX - tw // 2, lock_y + m_h + 26), label, font=font, fill=BEET)

cover.save("social/facebook-event.png")
cover.save("social/facebook-event.jpg", quality=88, optimize=True)
print("wrote social/facebook-event.png and .jpg  band h=%d top=%d" % (band.height, H - band.height))
