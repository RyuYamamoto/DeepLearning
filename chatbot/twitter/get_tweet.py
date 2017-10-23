#!/usr/bin/python
#-*- coding: utf-8 -*-
import tweepy

#認証を行う
consumer_key = "YrGrqMp9MWbRuLLmOrgwv1rP8"
consumer_secret = "h6pZQZ8s4CLkst3yufOpTSJuvTP85gtxCvAYL3XOlvC5MSQiNt"
access_token = "854511352630530048-o2ZdJBNZjaAxmNL12aaxzUZnqNDAYkJ"
access_secret = "rZ1l43kOVrsREE7mfc84EO71oJp8Vr1HQTp3VCQJeZDXF"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

f = open("out.txt","w")

for p in tweepy.Cursor(api.user_timeline,id="@ryu_software").items(3200):
    f.write(p.text.encode('utf-8')+"\n")

f.close()
