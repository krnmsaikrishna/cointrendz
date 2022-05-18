from datetime import datetime
import json
import requests 
from pyrogram import Client, filters

print("Code Working")

app = Client(
    "bot",
    api_id    = 8793184,
    api_hash  = "2bd06ae25625234f0316b7a8e193bb6a"
    )

channel_1 = "cointrendz_whalehunter"
channel_2 = "cointrendz_wallmonitor"
channel_3 = "cointrendz_pumpdetector"

site_url = "http://cointrendz.ml/crypto/bot.php?type="


@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_1))
def my_handler(client, message):
  try:
   if "Activity" in message.text :
    _t = message.text 
    _t = _t.splitlines()
    data = {}
    data['coin']  = (_t[0].split(' ')[0]).split('/')[0]
    data['pair']  = (_t[0].split(' ')[0]).split('/')[1]
    data['type']  = _t[1].split(' ')[2]
    data['volu']  = _t[2].split(' ')[0]
    data['prch']  = (_t[3].split(' ')[3])[1:-2]
    data['price'] = _t[3].split(' ')[1]
    data['size']  = _t[4].split(' ')[2]
    data['24h']   = _t[6].split(' ')[2]
    data = json.dumps(data)
    req = requests.get(site_url+"spot&data="+data)
    #print(req.text)
  except Exception as e:
    print("Error :: Spot Module ::"+e.message)





@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_2))
def my_handler(client, message):
  try:
   if "Wall" in message.text :
    _t = message.text 
    _t = _t.splitlines()
    data = {}
    data['coin']  = (_t[0].split(' ')[0]).split('/')[0]
    data['pair']  = (_t[0].split(' ')[0]).split('/')[1]
    data['type']  = _t[1].split(' ')[0]
    data['vol']   = _t[2].split(' ')[0]
    data['price'] = _t[2].split(' ')[3]
    data['size']  = _t[3].split(' ')[2]
    data['24h']   = _t[4].split(' ')[2]
    data = json.dumps(data)
    req = requests.get(site_url+"wall&data="+data)
    #print(req.text)
  except Exception as e:
    print("Error :: Wall Module ::"+e.message)



@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_3))
def my_handler(client, message):
  try:
   if "Pumping" in message.text :
    _t = message.text 
    _t = _t.splitlines()
    data = {}
    data['coin']  = (_t[0].split(' ')[2]).split('/')[0]
    data['pair']  = (_t[0].split(' ')[2]).split('/')[1]
    data['price'] = _t[1].split(' ')[1]
    data['vol']   =_t[2].split(' ')[1]
    data['prich'] = (_t[1].split(' ')[3])[2:-2]
    data['volch'] = (_t[2].split(' ')[3])[2:-2]
    data = json.dumps(data)
    req = requests.get(site_url+"pump&data="+data)
    #print(req.text)
  except Exception as e:
    print("Error :: Pump Module ::"+e.message)
    
app.run()
