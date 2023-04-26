import telebot
from telebot import types

bot = telebot.TeleBot('6259643431:AAF9IgFc_zkZ7R5_IENYr7c-4xHxsxxVgxc')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Это первый тест одиссейки на новом боте. Пока что доступен только 8А(и то только для тайлорины) Это является показательным ботом для вас))) Введите 8А", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='8А', txt='312')
    btn2 = types.InlineKeyboardButton(text='8Б', txt='215')
    btn3 = types.InlineKeyboardButton(text='8В', txt='110')
    btn4 = types.InlineKeyboardButton(text='8Г', txt='210')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.from_user.id, "Выберите класс", reply_markup = markup)
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Чё не так?', reply_markup=markup) #ответ бота
    elif message.text == '8А':
        bot.send_message(message.from_user.id, 'Ну, это, я преувеличил. Но я это могу. Крч, для вас доступ бесплатный и преждевременный. Хорошего дня')
    elif message.text == 'Мама':
        bot.send_message(message.from_user.id, 'Я тебя люблю!!!')
    elif message.text == 'Деда':
        bot.send_message(message.from_user.id, 'бубубубубу')
bot.polling(none_stop=True, interval=0)