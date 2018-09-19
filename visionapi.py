#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:05:49 2018

@author: wangyuying
"""

import io
import os
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image,ImageDraw,ImageFont

# export GOOGLE_APPLICATION_CREDENTIALS="/Users/wangyuying/Desktop/twitter_image/602miniproject-715c853df0e2.json"
client = vision.ImageAnnotatorClient()

path = '/Users/wangyuying/Desktop/twitter_image'
file_list = os.listdir(path)
print(file_list)

for file_name in file_list:
    with io.open(file_name,'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    img_text=[]
    for label in labels:
        img_text.append(label.description)
        print(label.description)
    print(img_text)
    img_text_draw = str(img_text[:5])
    print(img_text_draw)
    if os.path.splitext(file_name)[1] == '.jpg':
        print(file_name)
        imdraw = Image.open(file_name)
        draw = ImageDraw.Draw(imdraw)
        font = ImageFont.truetype('/Users/wangyuying/Desktop/twitter_image/cmss10.ttf', 20)
        draw.text((10,10),text=img_text_draw,font=font)
        imdraw.save(file_name)
        
