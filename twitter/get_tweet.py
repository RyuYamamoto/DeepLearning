from requests_oauthlib import  OAuth1Session
import json
import time
import pandas as pd

CK="YrGrqMp9MWbRuLLmOrgwv1rP8"
CS="h6pZQZ8s4CLkst3yufOpTSJuvTP85gtxCvAYL3XOlvC5MSQiNt"
AT="854511352630530048-o2ZdJBNZjaAxmNL12aaxzUZnqNDAYkJ"
AS="rZ1l43kOVrsREE7mfc84EO71oJp8Vr1HQTp3VCQJeZDXF"

url = "https://api.twitter.com/1.1/statuses/update.json"

params = {'count': 100}

TweetList = []

twitter = OAuth1Session(CK, CS, AT, AS)

for i in range(100):
    req = twitter.get(url, params = params)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            TweetList.append(tweet["text"])
    else:
        print ("Error: %d" % req.status_code)
	time.sleep(60)

df = pd.DataFrame(TweetList)
df.to_csv('tweetlist.csv')
