# -*- coding: utf-8 -*-
"""Creates the link-preview images (1200x630) in assets/. Run once: python3 make_og.py"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
TEXT = {
    "en": ("Less waste.", "More profit.", "AI-powered e-commerce profit partner · Free check-up"),
    "tr": ("Daha az israf.", "Daha fazla kâr.", "AI destekli e-ticaret kâr ortağınız · Ücretsiz check-up"),
}

for lang, (l1, l2, sub) in TEXT.items():
    im = Image.new("RGB", (1200, 630), "#0E1A2B")
    d = ImageDraw.Draw(im)
    d.text((80, 70), "AI Trade", font=ImageFont.truetype(BOLD, 40), fill="#FFFFFF")
    big = ImageFont.truetype(BOLD, 96)
    d.text((80, 200), l1, font=big, fill="#FFFFFF")
    d.text((80, 310), l2, font=big, fill="#F59E0B")
    d.text((80, 470), sub, font=ImageFont.truetype(REG, 32), fill="#C9D1DC")
    # small rising line, echoing the hero chart
    pts = [(820, 150), (880, 146), (940, 152), (1000, 120), (1060, 96), (1120, 80)]
    d.line(pts, fill="#F59E0B", width=6, joint="curve")
    im.save(os.path.join(HERE, "assets", "og-%s.png" % lang), optimize=True)
print("ok")
