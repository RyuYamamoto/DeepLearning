#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pya3rt

apikey = ""
client = pya3rt.TalkClient(apikey)

while True:
    input_reply = input_raw(">> ")
    result = client.talk(input_reply)
    print result['results'][0]['reply']

