#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy

# 各種キーをセット
CONSUMER_KEY = 'YrGrqMp9MWbRuLLmOrgwv1rP8'
CONSUMER_SECRET = 'h6pZQZ8s4CLkst3yufOpTSJuvTP85gtxCvAYL3XOlvC5MSQiNt'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '854511352630530048-o2ZdJBNZjaAxmNL12aaxzUZnqNDAYkJ'
ACCESS_SECRET = 'rZ1l43kOVrsREE7mfc84EO71oJp8Vr1HQTp3VCQJeZDXF'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')
