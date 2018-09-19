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


consumer_key = 'secret'
consumer_secret = 'secret'
access_token = 'secret'
access_secret = 'secret'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)



results = api.user_timeline(id="@BU_Tweets", count=200)

tweets_with_media = set()
for tweet in results:
    media = tweet.entities.get('media',[])
    if (len(media)>0):
        tweets_with_media.add(media[0]['media_url'])
        

for url in tweets_with_media:
    wget.download(url)

# change iamges name
    
path = '/Users/wangyuying/Desktop/twitter_image'
filelist = os.listdir(path)
i = 0

for files in filelist:
    i = i+1
    olddir = os.path.join(path,files)
    if os.path.splitext(files)[1] == '.jpg':
        newname = os.path.join(path,str(i-1)+'.jpg')
        os.rename(olddir,newname)

