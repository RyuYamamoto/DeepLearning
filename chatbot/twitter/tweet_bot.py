#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import re
import os
import json
import requests 
import tweepy
import datetime
import settings

payload = {
  "utt": "",
  "context": "",
  "nickname": "",
  "mode": "dialog"
}

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
 
api = tweepy.API(auth) 

capture = cv2.VideoCapture(0)

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += datetime.timedelta(hours=9)

        # リプライが来たら返信
        if str(status.in_reply_to_screen_name)=="bot_api_ai":# and str(status.user.screen_name)=="{Twitter_ID}":
            if str(status.text) == u"@bot_api_ai photo":
                print "OK"
                ret, frame = capture.read()
                path = "photo.png"
                cv2.imwrite(path,frame)
                tweet = "@" + str(status.user.screen_name) + "\n"
                api.update_with_media(filename="photo.png", status=tweet)
                os.remove(path)
            else:
                payload['utt'] = re.sub("@bot_api_ai ", "",status.text)
                payload['nickname'] = status.user.screen_name
                url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='+settings.API_KEY
                r = requests.post(url, data=json.dumps(payload))
                res_json = r.json()
                payload['context'] = res_json['context']

                status_id=status.id
                tweet = "@" + str(status.user.screen_name) + " " + res_json['utt'].encode('utf-8') + "\n"
                api.update_status(status=tweet, in_reply_to_status_id=status_id)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
     
    def on_timeout(self):
        print('Timeout...')
        return True

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()

capture.release()
cv2.destroyAllWindows()
