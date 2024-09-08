import requests
import asyncio
from aiogram import Bot
import time


#Enter Your Bot Token
bot_token=""

#Enter Your Chat Id
chat_ids=["", ""]

bot = Bot(token=bot_token)

async def send_telegram_message(text):
    for chat_id in chat_ids:
        await bot.send_message(chat_id=chat_id, text=text) 



print('Bot Started, You will receive notifications once gas fee got to required level\n')

# Define the API endpoint
url = 'https://mempool.space/api/v1/fees/recommended'

while(True):

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        
        # Print the fetched data
        print('Current Gas fee -', data.get('economyFee'))
        gas=data.get('economyFee')
    else:
        print("API error")
        continue

    if gas<=2:
        asyncio.run(send_telegram_message(f"Low Bitcoin Gas Fee!!! Current Gas fee is {gas} sats"))
        time.sleep(60)
    else:
        time.sleep(5)
