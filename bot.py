import base64
import json
import re
from pyrogram import Client, filters
from pyrogram.methods.messages import edit_inline_media
#from pyrogram.types import User, Message
#from pyrogram.types import ChatPermissions

#  bot_token = "5020987340:AAFRWHMCTiXZNMnOdFrtH1znJ-WGvc_uXaA"

print("ok boss")

app = Client(
    "boss",
    api_id    = 8793184,
    api_hash  = "2bd06ae25625234f0316b7a8e193bb6a"
    )

@app.on_message(filters.channel  &  filters.create(lambda client,message : message.username == "nsim_channel"))
def my_handler(client, message):
    print(message.text)
app.run()
