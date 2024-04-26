#импортировать нашу библиотеку и подключить токен бота:
import telebot
bot = telebot.TeleBot('6173671667:AAFIrvHOq3foGWP9j9qk0bmRxLhHjIgSKyY')

#объявить метод для получения текстовых сообщений
#объявили слушателя для текстовых сообщений и метод их обработки
@bot.message_handler(content_types=['text'])
def get_text_message(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id,"Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
		bot.send_message(message.from_user.id,"Напиши привет")
	else:
		bot.send_message(message.from_user.id,"Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)