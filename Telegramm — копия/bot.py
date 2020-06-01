import telebot
import config
from telebot import types
import time

bot = telebot.TeleBot(config.TOKEN)  # Создаю класс, который делает всё тоже самое, что и модуль, забирая токен из файла конфига


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Что ты умеешь?🤔")
    markup.add(item1)

    bot.send_message(message.chat.id, "Привет, я помошник мистера Глалсе.",
    	parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, "Что тебе нужно?",
    	parse_mode='html')

@bot.message_handler(content_types=['text'])
def about(message):
        if message.text == "Что ты умеешь?🤔":
            global IP
            IP = message.chat.id
            
            print(IP)
            bot.send_message(message.chat.id, "Итак, меня зовут mr.Sodal))", parse_mode='html')
            time.sleep(2)
            bot.send_message(message.chat.id, "Я сам себе имя придумал))", parse_mode='html')
            time.sleep(1)
            bot.send_message(message.chat.id, "Я был создан каким-то дебилом по кличке Dasokrys для того, чтобы помогать Mr.Glalse", parse_mode='html')
            time.sleep(5)
            bot.send_message(message.chat.id, "Пока что я могу:", parse_mode='html')  
            time.sleep(1)
            bot.send_message(message.chat.id, "Напомнить тебе, о новых роликах на канале", parse_mode='html')
            bot.send_message(message.chat.id, "Помочь тебе найти его канал", parse_mode='html')
            bot.send_message(message.chat.id, "Но мой функционал постоянно увеличивается, так что скоро я смогу делать ещё больше!🤩", parse_mode='html')
            time.sleep(7)

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Понятно", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Ну что?", parse_mode='html', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Молодец 😎')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton("ОК")
            markup.add(item)
            bot.send_message(call.message.chat.id, 'Чтобы продолжить нажми ОК', reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ну что?",
                reply_markup=None)
        elif call.data == 'bad':
            bot.send_message(call.message.chat.id, 'Ну прочита ещё раз 😣')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton("ОК")
            markup.add(item)
            bot.send_message(call.message.chat.id, 'Чтобы продолжить нажми ОК', reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ну что?",
                reply_markup=None)



bot.polling(none_stop = True)
