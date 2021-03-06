#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# Read the whole text.
# text = open(path.join(d, 'alice.txt')).read()
text = open('../pywx/wx_singnature.txt', encoding='utf-8').read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
coloring = np.array(Image.open("../pywx/alice.png"))

wc = WordCloud(
    background_color="white",
    max_words=2000,
    mask=coloring,
    max_font_size=40,
    random_state=42,
    font_path=r"C:\simhei.ttf"
)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(coloring)

# show
# The pil way (if you don't have matplotlib)
image = wc.to_file('./wds.jpg')
