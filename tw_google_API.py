#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import wget
import io
import os
import pymysql
import pymongo
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw, ImageFont


consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


def tw_download(tw_id, tw_num):
    # authorize twitter
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    results = api.user_timeline(id=tw_id, count=tw_num)  # id = @BU_Tweets,@taylorswift13
    path = '/Users/wangyuying/Desktop/twitter_image/pics/' + tw_id
    os.mkdir(path)
    os.chdir(path)
    tweets = set()
    for tweet in results:
        media = tweet.entities.get('media', [])
        if (len(media) > 0):
            tweets.add(media[0]['media_url'])
    for url in tweets:
        wget.download(url)

    # change iamges name
    filelist = os.listdir(path)
    i = 0
    img_num = 0
    for files in filelist:
        olddir = os.path.join(path, files)
        if os.path.splitext(files)[1] == '.jpg':
            img_num += 1
            newname = os.path.join(path, str(i) + '.jpg')
            i += 1
            os.rename(olddir, newname)
    print('\n')
    print('There are {} images you have downloaded'.format(img_num))
    return img_num


def get_draw_label(tw_id):
    # export GOOGLE_APPLICATION_CREDENTIALS="/Users/wangyuying/Desktop/twitter_image/602miniproject-715c853df0e2.json"
    client = vision.ImageAnnotatorClient()
    path = '/Users/wangyuying/Desktop/twitter_image/pics/' + tw_id

    file_list = os.listdir(path)
    label_dic = {}
    for file_name in file_list:
        if file_name.endswith(".jpg"):
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()
            image = types.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
            img_text = []
            for label in labels:
                img_text.append(label.description)
            label_dic[file_name] = list(img_text[:5])
            img_text_draw = str(img_text[:5])
            imdraw = Image.open(file_name)
            draw = ImageDraw.Draw(imdraw)
            font = ImageFont.truetype('/Users/wangyuying/Desktop/twitter_image/cmss10.ttf', 20)
            draw.text((10, 10), text=img_text_draw, font=font)
            imdraw.save(file_name)

    return label_dic


def store_mysqldb(tw_id, img_num, label_dic):
    try:
        twdb = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="tw"
        )
    except Exception:
        print("having trouble connecting MySQL database...")

    cursor = twdb.cursor()
    sql_1 = "INSERT INTO tw_info(twID, num, filename, label1, label2, label3, label4, label5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    for key, value in label_dic.items():
        if len(value) < 5:
            tmp_list = ['None'] * (5 - len(value))
            value.extend(tmp_list)
        cursor.execute(sql_1, (tw_id, img_num, key, value[0], value[1], value[2], value[3], value[4]))
        twdb.commit()
    print("Finishing storing mysql database")


def store_mongodb(tw_id, img_num, label_dic):
    client = pymongo.MongoClient("")

    twdb = client.tw  # database
    tw_info = twdb.twinfo  # collection
    for key, value in label_dic.items():
        # print(key)
        # print(value)
        if len(value) < 5:
            tmp_list = ['None'] * (5 - len(value))
            value.extend(tmp_list)
        nosql = {"twID": tw_id, "num": img_num, "filename": key, "label1": value[0], "label2": value[1], "label3": value[2], "label4": value[3], "label5": value[4]}
        tw_info.insert_one(nosql)

    print("Finishing storing MongoDB")


if __name__ == '__main__':
    print("Please input twiiter ID")
    tw_id = str(input())
    print("Please input the number of tweets that you want to download")
    tw_num = int(input())
    img_num = tw_download(tw_id, tw_num)
    label_dic = get_draw_label(tw_id)
    # store_mysqldb(tw_id, img_num, label_dic)
    store_mongodb(tw_id, img_num, label_dic)
