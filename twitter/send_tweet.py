# coding: utf-8
from requests_oauthlib import  OAuth1Session
import json
import time
import pandas as pd

CK = '3Np53J0MGrKE0e5VN4k6mhqux'
CS = 'ci05sJ1IlGODvsN40KVd4h5OxFwlA1o04lpwC19NYkaJnLpO31'
AT = '2694221550-LDWM5LfSsXnEwQb6K2xoMk7YFiuSYSdT0rc7JO5'
AS = 'zUUi8pxsAFeIdAhY8OU81xAaDhQWj6uITQphrWPAS1woA'

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "テスト中です"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
