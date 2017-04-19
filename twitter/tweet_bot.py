#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tweepy
import datetime
 
CK="YrGrqMp9MWbRuLLmOrgwv1rP8"
CS="h6pZQZ8s4CLkst3yufOpTSJuvTP85gtxCvAYL3XOlvC5MSQiNt"
AT="854511352630530048-o2ZdJBNZjaAxmNL12aaxzUZnqNDAYkJ"
AS="rZ1l43kOVrsREE7mfc84EO71oJp8Vr1HQTp3VCQJeZDXF"
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
api = tweepy.API(auth)
 
class Listener(tweepy.StreamListener):
    def on_status(self, status):
		status.created_at += datetime.timedelta(hours=9)
		if str(status.in_reply_to_screen_name)==api.me().screen_name and str(status.user.screen_name)=="seana_ps56":
			tweet = "@" + str(status.user.screen_name) + " " + "Hello！\n" + str(datetime.datetime.today())
			api.update_status(status=tweet)
			return True
      
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
      
    def on_timeout(self):
        print('Timeout...')
        return True
  
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
  
listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()
