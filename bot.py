from datetime import datetime
import json
import requests 
from pyrogram import Client, filters

print("Code Working")

app = Client(
    "boss",
    api_id    = 8793184,
    api_hash  = "2bd06ae25625234f0316b7a8e193bb6a"
    )

channel_1 = "cointrendz_whalehunter"
channel_2 = "cointrendz_wallmonitor"
channel_3 = "cointrendz_pumpdetector"

site_url = "http://cointrendz.ml/bot.php?type="


def _o(str,pos):
    return str.split(' ')[pos]


@app.on_message(filters.channel  &  filters.create(lambda _,__,query: query.chat.username == channel_1))
def my_handler(client, message):
  try:
    _t = message.text 
    _t = _t.splitlines()
    data = {}
    stam = datetime.fromtimestamp(message.date).strftime('%I:%M %p')
    data['stam']  = stam
    data['coin']  = _t[0].split(' ')[0]
    data['type']  = _t[1].split(' ')[2]
    data['volu']  = _t[2].split(' ')[0]
    data['prch']  = _t[3].split(' ')[1:-1]
    data['price'] = ' '.join(_t[3].split(' ')[1:3])
    data['size']  = ' '.join(_t[4].split(' ')[2:4])
    data['24h']   = _t[6].split(':')[1]
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
    stam = datetime.fromtimestamp(message.date).strftime('%I:%M %p')
    data['stam']  = stam
    data['coin']  = _t[0].split(' ')[0]
    data['type']  = _t[1].split(' ')[0]
    data['vol']   = _t[2].split('@')[0]
    data['price'] = _t[2].split('@')[1]
    data['size']  = _t[3].split(':')[1]
    data['24h']   = _t[4].split(':')[1]
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
    data['coin'] = _t[0].split(' ')[2]
    data['price'] = ' '.join(_t[1].split(' ')[1:3])
    data['prich'] = (_t[1].split(' ')[3])[1:-1]
    data['volch'] = (_t[2].split(' ')[3])[1:-1]
    data['vol'] =' '.join(_t[2].split(' ')[1:3])
    data = json.dumps(data)
    req = requests.get(site_url+"pump&data="+data)
    print(req.text)
  except:
    print("Error on Pump")
    
app.run()
