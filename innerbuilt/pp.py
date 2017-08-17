# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('1.png')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
#im.thumbnail((w//2, h//2))
#print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
#im.save('2.png', 'png')

#im = im.filter(ImageFilter.BLUR)
#im.save('blur.png', 'png')

#随机字母
def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64, 255), random.randint(64,255), random.randint(64,255))

def rndColorTwo():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255,255,255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font = font, fill=rndColorTwo())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')