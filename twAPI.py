#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:28:52 2018

@author: wangyuying
"""


#  -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import wget
import os
import pymysql
from datetime import datetime

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


def tw_download():
    # connect MySQL
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

    # authorize twitter
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # download images
    print("Please input your name")
    tw_user = str(input())
    print("Please input twiiter ID")
    tw_id = str(input())
    print("Please input the number of tweets that you want to download")
    tw_num = int(input())
    results = api.user_timeline(id=tw_id, count=tw_num)  # id = @BU_Tweets,Boston University
    path = '/Users/wangyuying/Desktop/twitter_image/pics'
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
            i = i + 1
            os.rename(olddir, newname)
    print('\n')
    print('There are {} images you have downloaded'.format(img_num))

    # Store database
    cursor = twdb.cursor()

    sql1 = "INSERT INTO img_num(twID, num, user, time) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(sql1, (tw_id, img_num, tw_user, datetime.now()))
        twdb.commit()
    except Exception:
        print("Wrong mysql command")

    print("Finishing storing mysql database")

    twdb.close()


if __name__ == '__main__':
    tw_download()
