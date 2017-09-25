# coding: utf-8

import requests
import json
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

API_KEY = '6957474e707a7468476f7943782f797a35384566367669796738743738594272783055354c384578735835'

@default_reply()
def default_func(message):
    payload = {
        "utt": "",
        "context": "",
        "nickname": "",
        "mode": "dialog"
    }
    payload['utt'] = message.body['text']
    url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='+API_KEY
    r = requests.post(url,data=json.dumps(payload))
    #res_json = r.json()
    #payload['context'] = res_json['context']
    #print res_json['utt'].encode('utf-8')
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
    #msg = 'あなたの送ったメッセージは\n```' + text.encode('utf-8') + '```'
    #message.reply(res_json['utt'].encode('utf-8'))      # メンション
    message.reply('熱盛')
'''
@default_reply()
def default_func(message):
    text = message.body['text'].encode('utf-8')
    payload['utt'] = text
    payload['nickname'] = status.user.screen_name
    url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='+API_KEY
    r = requests.post(url, data=json.dumps(payload),  verify=False)
    res_json = r.json()
    payload['context'] = res_json['context']
    message.reply(res_json['utt'].encode('utf-8')
'''