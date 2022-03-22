import base64
import json
import re
import requests 
from pyrogram import Client, filters
from pyrogram.methods.messages import edit_inline_media
#from pyrogram.types import User, Message
#from pyrogram.types import ChatPermissions

#bot_token = "5020987340:AAFRWHMCTiXZNMnOdFrtH1znJ-WGvc_uXaA"

print("Code Working")

app = Client(
    "boss",
    api_id    = 8793184,
    api_hash  = "2bd06ae25625234f0316b7a8e193bb6a"
    )

channel_1 = "cointrendz_whalehunter"
channel_2 = "cointrendz_wallmonitor"
channel_3 = "cointrendz_pumpdetector"

site_url = "https://mysgpa.me/coin/tel.php?type="


def _o(str,pos):
    return str.split(' ')[pos]


@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_1))
def my_handler(client, message):
  try:
    _t = message.text 
    _t = _t.splitlines()
    data = {}
    data['coin'] = _o(_t[0],0).split('/')[0]
    data['pair'] = _o(_t[0],0).split('/')[1]
    data['type'] = _o(_t[1],2)
    data['volu'] = _o(_t[2],0)
    data['price'] = _o(_t[3],1)
    data['size'] = _o(_t[4],2)
    data['day'] = _o(_t[6],2)
    data = json.dumps(data)
    req = requests.get(site_url+"spot&data="+data)
    print(req.text)
  except:
    print("Error on Spot")





@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_2))
def my_handler(client, message):
  try:
    _t = message.text 
    _t = _t.splitlines()
    
    data = {}
    data['coin'] = _o(_t[0],0).split('/')[0]
    data['pair'] = _o(_t[0],0).split('/')[1]
    data['type'] = _o(_t[1],0)
    data['volu'] = _o(_t[2],0)
    data['price'] = _o(_t[2],3)
    data['size'] = _o(_t[3],2)
    data['day'] = _o(_t[4],2)
    data = json.dumps(data)
    req = requests.get(site_url+"wall&data="+data)
    print(req.text)
  except:
    print("Error on Wall")



@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_3))
def my_handler(client, message):
  try:
    _t = message.text 
    _t = _t.splitlines()
    data = {}
    data['coin'] = _o(_t[0],2).split('/')[0]
    data['pair'] = _o(_t[0],2).split('/')[1]
    data['price'] = _o(_t[1],1)
    data['change'] = _o(_t[1],3)
    data['vol'] = _o(_t[2],1)
    data['volup'] = _o(_t[2],3)
    data = json.dumps(data)
    req = requests.get(site_url+"pump&data="+data)
    print(req.text)
  except:
    print("Error on Pump")
    
app.run()
