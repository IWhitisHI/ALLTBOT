import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Данил")
	item2 = types.KeyboardButton("Роман")
	item3 = types.KeyboardButton("Віталій")

	markup.add(item1, item2,item3)

	bot.send_message(message.chat.id, "Привіт!!!\nТи хто???",
		parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def whoareyou(message):
	if message.chat.type == 'private':
		if message.text == "Данил":

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.row('1d', '2d', '/start')

			bot.send_message(message.chat.id, "Який тиждень???", reply_markup=markup)

		elif message.text == "Роман":

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.row('1r', '2r', '/start')

			bot.send_message(message.chat.id, "Який тиждень???", reply_markup=markup)

		elif message.text == "Віталій":

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			markup.row('1v', '2v', '/start')

			bot.send_message(message.chat.id, "Який тиждень???", reply_markup=markup)

		elif message.text == "1d":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='1.1d')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='1.2d')
			item3 = types.InlineKeyboardButton("Середа", callback_data='1.3d')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='1.4d')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='1.5d')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='1wdALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)

		elif message.text == "2d":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='2.1d')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='2.2d')
			item3 = types.InlineKeyboardButton("Середа", callback_data='2.3d')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='2.4d')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='2.5d')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='2wdALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)


		elif message.text == "1r":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='1.1r')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='1.2r')
			item3 = types.InlineKeyboardButton("Середа", callback_data='1.3r')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='1.4r')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='1.5r')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='1wrALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)

		elif message.text == "2r":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='2.1r')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='2.2r')
			item3 = types.InlineKeyboardButton("Середа", callback_data='2.3r')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='2.4r')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='2.5r')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='2wrALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)

		elif message.text == "1v":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='1.1v')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='1.2v')
			item3 = types.InlineKeyboardButton("Середа", callback_data='1.3v')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='1.4v')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='1.5v')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='1wvALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)

		elif message.text == "2v":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Понеділок", callback_data='2.1v')
			item2 = types.InlineKeyboardButton("Вівторок", callback_data='2.2v')
			item3 = types.InlineKeyboardButton("Середа", callback_data='2.3v')
			item4 = types.InlineKeyboardButton("Четверг", callback_data='2.4v')
			item5 = types.InlineKeyboardButton("П'ятниця", callback_data='2.5v')
			item6 = types.InlineKeyboardButton("Ввесь тиждень", callback_data='2wvALL')

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "Який день???", reply_markup=markup)

		else:
			bot.send_message(message.chat.id, '"Текст" ВВОДИТИ НЕМОЖНА!!!')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == "1wvALL":
				bot.send_message(call.message.chat.id, "Віталій\n------------------------1ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА: Англ.--АУДИТОРІИЯ: 11.415\nВівторок:\n1 ПАРА:\n2 ПАРА: Історія--АУДИТОРІИЯ: 3.112\n3 ПАРА: Електромех-АУДИТОРІИЯ: 10.104\n4 ПАРА: Фіз-ра\nСереда:\n1 ПАРА:\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n4 ПАРА:\nЧетверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\nП'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА:")		
			elif call.data == '2wvALL':
				bot.send_message(call.message.chat.id, "Віталій\n------------------------2ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА: \nВівторок:\n1 ПАРА:\n2 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Історія(Л)--АУДИТОРІИЯ: 4.201\n4 ПАРА: \nСереда:\n1 ПАРА:\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n4 ПАРА:\nЧетверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\nП'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА: Вишка--АУДИТОРІИЯ: 3.112")
			elif call.data == "1wdALL":
				bot.send_message(call.message.chat.id, "-------------------------Данил-----------------------\n------------------------1ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: \n3 ПАРА: Історія--АУДИТОРІИЯ: 3.120\n4 ПАРА: Electrical--АУДИТОРІИЯ: 5.518\nВівторок:\n1 ПАРА:\n2 ПАРА: \n3 ПАРА: Інженерка-АУДИТОРІИЯ: 11.314\n4 ПАРА: Інженерка-АУДИТОРІИЯ: 11.314\nСереда:\n1 ПАРА: Англ.--АУДИТОРІИЯ: 11.313\n2 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n3 ПАРА: Фіз-ра\n4 ПАРА: Фізика(П)--АУДИТОРІИЯ: 1.357\nЧетверг:\n1 ПАРА: Історія(л)--АУДИТОРІИЯ: 4.203\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 4.203\n3 ПАРА:\n4 ПАРА:\nП'ятниця:\n1 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 1.002\n2 ПАРА: Electrical--АУДИТОРІИЯ 8.103\n3 ПАРА: Вишка--АУДИТОРІИЯ: 3.102\n4 ПАРА:")
			elif call.data == '2wdALL':
				bot.send_message(call.message.chat.id, "-------------------------Данил-----------------------\n------------------------2ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІЯ: 4.201\n3 ПАРА: Вишка--АУДИТОРІИЯ: 3.410\n4 ПАРА: \nВівторок:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.423\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.423\nСереда:\n1 ПАРА: Англ.--АУДИТОРІИЯ: 11.313 \n2 ПАРА: Electrical--АУДИТОРІИЯ: 5.118\n3 ПАРА: Інженерка--АУДИТОРІИЯ: 11.314\n4 ПАРА:\nЧетверг:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 4.201\n3 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n4 ПАРА:\nП'ятниця:\n1 ПАРА: Фізика(Л)--АУДИТОРІИЯ 1.002\n2 ПАРА: Electrical(Л)--АУДИТОРІИЯ: 8.103\n3 ПАРА: Фізика(П)--АУДИТОРІИЯ: 1.364\n4 ПАРА: FOP")
			elif call.data == "1wrALL":
				bot.send_message(call.message.chat.id, "-------------------------Роман-----------------------\n------------------------1ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІЯ: 3.102\n3 ПАРА: Вишка(П)--АУДИТОРІЯ: 3.410\n4 ПАРА: Прога(Л)--АУДИТОРІИЯ: 3.402\nВівторок:\n1 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n2 ПАРА: Фізика--АУДИТОРІИЯ: 1.431\n3 ПАРА: Фізика(П)--АУДИТОРІИЯ: 1.422\n4 ПАРА:\nСереда:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.102\n4 ПАРА: Теорія(П)--АУДТОРІЯ: 3.405\n5 ПАРА: Теорія(П)--АУДТОРІЯ: 3.405\nЧетверг:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Теорія(Л)--АУДТОРІЯ: 3.403\n4 ПАРА: Фіз-ра\nП'ятниця:\n1 ПАРА: Прога(Л)--АУДИТОРІИЯ: 3.402\n2 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n3 ПАРА:\n4 ПАРА:")
			elif call.data == '2wrALL':
				bot.send_message(call.message.chat.id, "-------------------------Роман-----------------------\n------------------------2ТИЖДЕНЬ----------------------\nПонеділок:\n1 ПАРА: Вишка(П)--АУДИТОРІИЯ: 3.102\n2 ПАРА: Вишка(Л)--АУДИТОРІЯ: 3.102\n3 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n4 ПАРА: \nВівторок:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Історія(Л)--АУДИТОРІИЯ: 4.201\n4 ПАРА: Англ.--АУДИТОРІИЯ: 8.1110а\nСереда:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.102\n4 ПАРА: Теорія(П)--АУДИТОРІИЯ: 3.405\nЧетверг:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Теорія(Л)--АУДИТОРІИЯ: 3.403\n4 ПАРА: Теорія--АУДИТОРІИЯ: 3.409\nП'ятниця:\n1 ПАРА: Прога(Л)--АУДИТОРІИЯ 3.402\n2 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n3 ПАРА: Історія(П)--АУДИТОРІИЯ: 3.210\n4 ПАРА:")
			elif call.data == '1.1d':
				bot.send_message(call.message.chat.id, "Понеділок:\n1 ПАРА:\n2 ПАРА: \n3 ПАРА: Історія--АУДИТОРІИЯ: 3.120\n4 ПАРА: Electrical--АУДИТОРІИЯ: 5.518\n")
			elif call.data == '1.2d':
				bot.send_message(call.message.chat.id, 'Вівторок:\n1 ПАРА:\n2 ПАРА: \n3 ПАРА: Інженерка-АУДИТОРІИЯ: 11.314\n4 ПАРА: Інженерка-АУДИТОРІИЯ: 11.314\n')
			elif call.data == '1.3d':
				bot.send_message(call.message.chat.id, 'Середа:\n1 ПАРА: Англ.--АУДИТОРІИЯ: 11.313\n2 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n3 ПАРА: Фіз-ра\n4 ПАРА: Фізика(П)--АУДИТОРІИЯ: 1.357\n')
			elif call.data == '1.4d':
				bot.send_message(call.message.chat.id, 'Четверг:\n1 ПАРА: Історія(л)--АУДИТОРІИЯ: 4.203\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 4.203\n3 ПАРА:\n4 ПАРА:\n')
			elif call.data == '1.5d':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 1.002\n2 ПАРА: Electrical--АУДИТОРІИЯ 8.103\n3 ПАРА: Вишка--АУДИТОРІИЯ: 3.102\n4 ПАРА:")
			elif call.data == '2.1d':
				bot.send_message(call.message.chat.id, "Понеділок:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІЯ: 4.201\n3 ПАРА: Вишка--АУДИТОРІИЯ: 3.410\n4 ПАРА: \n")
			elif call.data == '2.2d':
				bot.send_message(call.message.chat.id, "Вівторок:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.423\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.423\n")
			elif call.data == '2.3d':
				bot.send_message(call.message.chat.id, "Середа:\n1 ПАРА: Англ.--АУДИТОРІИЯ: 11.313 \n2 ПАРА: Electrical--АУДИТОРІИЯ: 5.118\n3 ПАРА: Інженерка--АУДИТОРІИЯ: 11.314\n4 ПАРА:\n")
			elif call.data == '2.4d':
				bot.send_message(call.message.chat.id, "Четверг:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 4.201\n3 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n4 ПАРА:\n")
			elif call.data == '2.5d':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА: Фізика(Л)--АУДИТОРІИЯ 1.002\n2 ПАРА: Electrical(Л)--АУДИТОРІИЯ: 8.103\n3 ПАРА: Фізика(П)--АУДИТОРІИЯ: 1.364\n4 ПАРА: FOP")
			elif call.data == '1.1r':
				bot.send_message(call.message.chat.id, "Понеділок:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІЯ: 3.102\n3 ПАРА: Вишка(П)--АУДИТОРІЯ: 3.410\n4 ПАРА: Прога(Л)--АУДИТОРІИЯ: 3.402\n")
			elif call.data == '1.2r':
				bot.send_message(call.message.chat.id, "Вівторок:\n1 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n2 ПАРА: Фізика--АУДИТОРІИЯ: 1.431\n3 ПАРА: Фізика(П)--АУДИТОРІИЯ: 1.422\n4 ПАРА:\n")
			elif call.data == '1.3r':
				bot.send_message(call.message.chat.id, "Середа:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.102\n4 ПАРА: Теорія(П)--АУДТОРІЯ: 3.405\n5 ПАРА: Теорія(П)--АУДТОРІЯ: 3.405\n")
			elif call.data == '1.4r':
				bot.send_message(call.message.chat.id, "Четверг:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Теорія(Л)--АУДТОРІЯ: 3.403\n4 ПАРА: Фіз-ра\n")
			elif call.data == '1.5r':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА: Прога(Л)--АУДИТОРІИЯ: 3.402\n2 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n3 ПАРА:\n4 ПАРА:")
			elif call.data == '2.1r':
				bot.send_message(call.message.chat.id, "Понеділок:\n1 ПАРА: Вишка(П)--АУДИТОРІИЯ: 3.102\n2 ПАРА: Вишка(Л)--АУДИТОРІЯ: 3.102\n3 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n4 ПАРА: \n")
			elif call.data == '2.2r':
				bot.send_message(call.message.chat.id, "Вівторок:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Історія(Л)--АУДИТОРІИЯ: 4.201\n4 ПАРА: Англ.--АУДИТОРІИЯ: 8.1110а\n")
			elif call.data == '2.3r':
				bot.send_message(call.message.chat.id, "Середа:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.102\n4 ПАРА: Теорія(П)--АУДИТОРІИЯ: 3.405\n")
			elif call.data == '2.4r':
				bot.send_message(call.message.chat.id, "Четверг:\n1 ПАРА:\n2 ПАРА:\n3 ПАРА: Теорія(Л)--АУДИТОРІИЯ: 3.403\n4 ПАРА: Теорія--АУДИТОРІИЯ: 3.409\n")
			elif call.data == '2.5r':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА: Прога(Л)--АУДИТОРІИЯ 3.402\n2 ПАРА: Прога--АУДИТОРІИЯ: 3.409\n3 ПАРА: Історія(П)--АУДИТОРІИЯ: 3.210\n4 ПАРА:")
			elif call.data == '1.1v':
				bot.send_message(call.message.chat.id, "Понеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІИЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА: Англ.--АУДИТОРІИЯ: 11.415\n")
			elif call.data == '1.2v':
				bot.send_message(call.message.chat.id, "Вівторок:\n1 ПАРА:\n2 ПАРА: Історія--АУДИТОРІИЯ: 3.112\n3 ПАРА: Електромех-АУДИТОРІИЯ: 10.104\n4 ПАРА: Фіз-ра\n")
			elif call.data == '1.3v':
				bot.send_message(call.message.chat.id, "Середа:\n1 ПАРА:\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n4 ПАРА:\n")
			elif call.data == '1.4v':
				bot.send_message(call.message.chat.id, "Четверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n")
			elif call.data == '1.5v':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА:")
			elif call.data == '2.1v':
				bot.send_message(call.message.chat.id, "Понеділок:\n1 ПАРА:\n2 ПАРА: Вишка--АУДИТОРІЯ: 3.120\n3 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.120\n4 ПАРА: \n")
			elif call.data == '2.2v':
				bot.send_message(call.message.chat.id, "Вівторок:\n1 ПАРА:\n2 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Історія(Л)--АУДИТОРІИЯ: 4.201\n4 ПАРА: \n")
			elif call.data == '2.3v':
				bot.send_message(call.message.chat.id, "Середа:\n1 ПАРА:\n2 ПАРА: Прога(Л)--АУДИТОРІИЯ: 5.407\n3 ПАРА: Прога--АУДИТОРІИЯ: 5.409\n4 ПАРА:\n")
			elif call.data == '2.4v':
				bot.send_message(call.message.chat.id, "Четверг:\n1 ПАРА:\n2 ПАРА: Електромех--АУДИТОРІИЯ: 5.203\n3 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n4 ПАРА: Фізика--АУДИТОРІИЯ: 1.429\n")
			elif call.data == '2.5v':
				bot.send_message(call.message.chat.id, "П'ятниця:\n1 ПАРА:\n2 ПАРА: Вишка(Л)--АУДИТОРІИЯ: 3.112\n3 ПАРА: Фізика(Л)--АУДИТОРІИЯ: 3.112\n4 ПАРА: Вишка--АУДИТОРІИЯ: 3.112\n")
	except Exception as e:
		print(repr(e))

bot.polling(none_stop=True)