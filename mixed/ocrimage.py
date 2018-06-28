#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

from PIL import Image as PI
import pytesseract

image = PI.open('./img/im.jpg')
code = pytesseract.image_to_string(image)
print(code)