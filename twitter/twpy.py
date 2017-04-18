#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy

# 各種キーをセット
CONSUMER_KEY = 'VZAGLM2i47wOTGjek2GaRte97'
CONSUMER_SECRET = 'HSpUa5ugKuGjScs06UstxVXnQAilGgHvFh0NYucOrWUNNtxuOt'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '838624603912060928-F5XznT95lFUVIniiGr3uSPcOodW91Ty'
ACCESS_SECRET = 'Xx0jKqS5Y4ZlWauKxD6NnnJPf9bfUvEShsH3MPTGGi8v1'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')
