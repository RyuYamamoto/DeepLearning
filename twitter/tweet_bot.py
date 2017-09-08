#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests 
import tweepy
import datetime
import settings

payload = {
  "utt": "",
  "context": "",
  "nickname": "",
  "nickname_y": "",
  "sex": "男",
  "bloodtype": "A",
  "birthdateY": "2017",
  "birthdateM": "1",
  "birthdateD": "20",
  "age": "26",
  "constellations": "水瓶座",
  "place": "東京",
  "mode": "dialog"
}

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
 
api = tweepy.API(auth) 

context_prev = ""

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += datetime.timedelta(hours=9)
        
        # リプライが来たら返信
        if str(status.in_reply_to_screen_name)=="bot_api_ai": #and str(status.user.screen_name)=="bot_api_ai":
            payload['utt'] = str(status.text)
            url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='+settings.API_KEY
            s = requests.session()
            r =  s.post(url, data=json.dumps(payload))
            res_json = json.loads(r.text)
            context_prev = res_json['context']
            tweet = "@" + str(status.user.screen_name) + " " + res_json['utt'].encode('utf-8')+"\n"
            api.update_status(status=tweet)
        return True
     
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
     
    def on_timeout(self):
        print('Timeout...')
        return True

#auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
#auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()
