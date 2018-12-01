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
from PIL import Image, ImageDraw, ImageFont
from twAPI import tw_download
import pymysql

# export GOOGLE_APPLICATION_CREDENTIALS="/Users/wangyuying/Desktop/twitter_image/602miniproject-715c853df0e2.json"

# tw_id = tw_download()
# print(tw_id)


client = vision.ImageAnnotatorClient()

path = '/Users/wangyuying/Desktop/twitter_image/pics'
file_list = os.listdir(path)
print(file_list)


def get_draw_label():
    tw_id = tw_download()
    print(tw_id)
    label_dic = {}
    for file_name in file_list:
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        img_text = []
        for label in labels:
            img_text.append(label.description)
        print(img_text)

        label_dic[file_name] = img_text
        img_text_draw = str(img_text[:5])
        if os.path.splitext(file_name)[1] == '.jpg':
            print(file_name)
            imdraw = Image.open(file_name)
            draw = ImageDraw.Draw(imdraw)
            font = ImageFont.truetype('/Users/wangyuying/Desktop/twitter_image/cmss10.ttf', 20)
            draw.text((10, 10), text=img_text_draw, font=font)
            imdraw.save(file_name)

    return label_dic, tw_id


def store_mysqldb():
    label_dic, tw_id = get_draw_label()
    try:
        twdb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Amber1129...",
            db="tw"
        )
    except Exception:
        print("having trouble connecting MySQL database...")

    cursor = twdb.cursor()
    sql_1 = "INSERT INTO tw_labels(twID, label, filename) VALUES (%s, %s, %s)"
    for key, value in label_dic.items():
        for label in label_dic[key]:
            cursor.execute(sql_1, (tw_id, label, key))
            twdb.commit()
    print("Finishing storing mysql database")


if __name__ == '__main__':
    get_draw_label()
    store_mysqldb()
