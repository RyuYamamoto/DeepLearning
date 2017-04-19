# coding: utf-8
from requests_oauthlib import  OAuth1Session
import json
import time
import pandas as pd

CK="YrGrqMp9MWbRuLLmOrgwv1rP8"
CS="h6pZQZ8s4CLkst3yufOpTSJuvTP85gtxCvAYL3XOlvC5MSQiNt"
AT="854511352630530048-o2ZdJBNZjaAxmNL12aaxzUZnqNDAYkJ"
AS="rZ1l43kOVrsREE7mfc84EO71oJp8Vr1HQTp3VCQJeZDXF"

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "hello."}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
