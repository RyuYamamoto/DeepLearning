# -*- coding: utf-8 -*-
import requests
import json
 
payload = {
  "utt": "はじめまして",
  "context": "",
  "nickname": "太郎",
  "nickname_y": "タロウ",
  "sex": "男",
  "bloodtype": "A",
  "birthdateY": "1990",
  "birthdateM": "1",
  "birthdateD": "20",
  "age": "26",
  "constellations": "水瓶座",
  "place": "北海道",
  "mode": "dialog"
}

APIKEY = ''
 
url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='
s = requests.session()
r =  s.post(url, data=json.dumps(payload))
 
res_json = json.loads(r.text)
print res_json['utt']
