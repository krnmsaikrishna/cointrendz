import os
import sys
import time
import asyncio
import json
import requests
from urllib import request

from telethon import TelegramClient, events, utils
from telethon.tl.functions.channels import JoinChannelRequest

session = 'bot'
api_id =  8793184
api_hash = '2bd06ae25625234f0316b7a8e193bb6a'
proxy = None
client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()

channel_1 ="https://t.me/nsim_channel"
channel_2 ="https://t.me/nsim_channel"
channel_3 ="https://t.me/nsim_channel"

def _o(str,pos):
    return str.split(' ')[pos]


"""
@client.on(events.NewMessage(chats=channel_1))
async def handler(event):  
    dt = str(event.date)
    _t = event.text
    _t = _t.splitlines()
    
    data = {}
    data["date"] = dt.split(" ")[0]
    data['coin'] = _o(_t[0],0).split('/')[0]
    data['pair'] = _o(_t[0],0).split('/')[1]
    data['type'] = _o(_t[1],2)
    data['volu'] = _o(_t[2],0)
    data['price'] = _o(_t[3],1)
    data['size'] = _o(_t[4],2)
    data['day'] = _o(_t[6],2)
    data = json.dumps(data)

    req = requests.get("https://mysgpa.me/coin/tel.php?type=spot&data="+data)
    print(req.text)

try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect() 


@client.on(events.NewMessage(chats=channel_2))
async def handler(event):  
    dt = str(event.date)
    _t = event.text
    _t = _t.splitlines()
    data = {}
    data["date"] = dt.split(" ")[0]
    data['coin'] = _o(_t[0],0).split('/')[0]
    data['pair'] = _o(_t[0],0).split('/')[1]
    data['type'] = _o(_t[1],0)
    data['volu'] = _o(_t[2],0)
    data['price'] = _o(_t[2],3)
    data['size'] = _o(_t[3],2)
    data['day'] = _o(_t[4],2)

    data = json.dumps(data)

    x = requests.get("https://mysgpa.me/coin/tel.php?type=wall&data="+data)
    print(x.text)

try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()

"""

@client.on(events.NewMessage(chats=channel_3))
async def handler(event):  
    dt = str(event.date)
    _t = event.text
    _t = _t.splitlines()
    data = {}
    data["date"] = dt.split(" ")[0]
    data['coin'] = _o(_t[0],2).split('/')[0]
    data['pair'] = _o(_t[0],2).split('/')[1]
    data['price'] = _o(_t[1],1)
    data['change'] = _o(_t[1],3)
    data['vol'] = _o(_t[2],1)
    data['volup'] = _o(_t[2],3)
    data = json.dumps(data)

    x = requests.get("https://mysgpa.me/coin/tel.php?type=pump&data="+data)
    print(x.text)

try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()
