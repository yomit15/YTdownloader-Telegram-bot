import os
import telebot
from pytube import YouTube

BOT_TOKEN = '6678492245:AAF0chojorPNydQfZxU2c93_xR8cn8qQ3SI'  # Replace with your bot token
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? Send me a YouTube link and I'll download the video for you!")


@bot.message_handler(func=lambda msg: msg.text is not None and "youtube.com" in msg.text)
def echo_all(message):
    url = message.text
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()  # Downloads to local directory
    bot.reply_to(message, "Video downloaded!")


bot.polling()
