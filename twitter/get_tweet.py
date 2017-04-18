from requests_oauthlib import  OAuth1Session
import json
import time
import pandas as pd

CK = '3Np53J0MGrKE0e5VN4k6mhqux'
CS = 'ci05sJ1IlGODvsN40KVd4h5OxFwlA1o04lpwC19NYkaJnLpO31'
AT = '2694221550-LDWM5LfSsXnEwQb6K2xoMk7YFiuSYSdT0rc7JO5'
AS = 'zUUi8pxsAFeIdAhY8OU81xAaDhQWj6uITQphrWPAS1woA'

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
