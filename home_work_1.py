#Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot


token = "********"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message,"Привет, чем могу помочь?")

@bot.message_handler(content_types=['text'])
def user_message(message):
    data = open('messages.text', 'a', encoding = 'utf-8')
    text = f'{message.from_user.username}: {message.text}'
    data.writelines(f'{text}\n')
    data.close
    bot.reply_to(message, 'Ожидайте, ваш запрос обрабатывается')
    

bot.infinity_polling()