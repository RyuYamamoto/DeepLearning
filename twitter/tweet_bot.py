#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tweepy
import datetime
 
CK="VZAGLM2i47wOTGjek2GaRte97"
CS="HSpUa5ugKuGjScs06UstxVXnQAilGgHvFh0NYucOrWUNNtxuOt"
AT="838624603912060928-F5XznT95lFUVIniiGr3uSPcOodW91Ty"
AS="Xx0jKqS5Y4ZlWauKxD6NnnJPf9bfUvEShsH3MPTGGi8v1"
 
# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
 
api = tweepy.API(auth)
 
class Listener(tweepy.StreamListener):
    def on_status(self, status):
		status.created_at += datetime.timedelta(hours=9)
		if str(status.in_reply_to_screen_name)=="AdultBrains" and str(status.user.screen_name)=="AdultBrains":
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
