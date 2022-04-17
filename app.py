import requests as r

import telebot, time, json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = "5397395609:AAFmwXvqtu4Yr19xdPb2_u_1Xdh5lqAId_U"
bot = telebot.TeleBot(token)

user_active = []

def getUrl(url):
	link_id = r.head(url, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
	get_data = r.get("https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B"+link_id+"%5D").text
	obj = json.loads(get_data)
	return obj["aweme_details"][0]["video"]["play_addr"]["url_list"][0];


@bot.message_handler(commands=['start'])
def start(message):
	chat_id = message.from_user.id
	username = message.from_user.username
	if username in user_active:
		print("sudah ada")
	else:
		user_active.append(username)
	print(username)
	bot.send_message(message.chat.id, "send me url tiktok")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
	pesan = message.text
	chat_id = message.from_user.id
	if "tiktok" in pesan:
		bot.send_video(chat_id, getUrl(pesan), caption = "terimakasi, jangan lupa share")
	elif pesan == "/useractive":
		for i in user_active:
			bot.send_message("5287615538", i)
	else:
		bot.send_message(chat_id, "send me url tiktok")

bot.polling()

