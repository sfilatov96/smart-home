# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper, types
import socket

ip = '124.195.19.18'
port = '1080'

apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip, port)
}

TOKEN = '563104187:AAGNNjXP4nFNstEB34HKVHcI1aaN8lVZV9Y'
bot = telebot.TeleBot(TOKEN)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def status(m):
    msg = "IP-адрес в локальной сети: {0}".format(get_ip_address())
    bot.send_message(m.chat.id, msg)


def choose_action(m):
    if m.text == "status":
        status(m=m)


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Привет, мой друг!')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['status']])
    msg = bot.send_message(
        m.chat.id, 'Выберите действие?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, choose_action)


bot.polling()
