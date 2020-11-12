import telebot
from telebot import apihelper
import time
import requests
import pprint

TOKEN = '1499614855:AAH-fSgCEvB1nx7tw1igrZdfU4uEviuaZhU'
BOT_URL = f' https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def command_start_function(message):
    bot.reply_to(message, 'Рад Вас приветствовать!')

@bot.message_handler(commands = ['help'])
def help_handler(message):
    bot.reply_to(message, 'Чем я могу вам помочь?')

@bot.message_handler(commands = ['admin'])
def admin_(message):
    if message.from_user.id == 336507536:
        bot.reply_to(message, 'Привет, создатель!')
    else:
        bot.reply_to(message, 'Я вас не знаю')

@bot.message_handler(content_types = ['text'])
def hello_text(message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'И тебе привет!')

@bot.message_handler(content_types = ['text'])
def how_do_text(message):
    if message.text.lower() == 'как дела':
        bot.reply_to(message, 'Хорошо. А у тебя?')

@bot.message_handler(content_types = ['text'])
def who_are_you_bot(message):
    if message.text.lower() == 'кто ты?':
        bot.reply_to(message, 'Я маленький бот, меня сделали, чтобы я помогал людям!')

@bot.message_handler(content_types = ['text'])
def by_text(message):
    if message.text.lower.lower() == 'до свидания':
        bot.reply_to(message, 'Заглядывай почаще')

bot.polling()
