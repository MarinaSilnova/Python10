#Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю

import telebot


token = "*********"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message,"Привет, чем могу помочь?")

@bot.message_handler(content_types=['text'])
def user_message(message):
    cur_id = str(message.from_user.id)
    data = open('first.text', 'w', encoding = 'utf-8')
    text = f'{cur_id}: {message.text}'
    data.writelines(f'{text}\n')
    data.close()
    data = open('first.text', 'r', encoding = 'utf-8')
    registration_list = data.readlines()
    data.close()
    for id in registration_list:
        print(id)
        answer = input('Введите ответ пользователю: ')
        bot.reply_to(message, answer)
        

bot.infinity_polling()