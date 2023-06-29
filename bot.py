
from telebot.async_telebot import AsyncTeleBot
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()


bot = AsyncTeleBot(os.environ.get('BOT_TOKEN')) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
	await bot.reply_to(message.chat.id, "Howdy, how are you doing?")
	

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())