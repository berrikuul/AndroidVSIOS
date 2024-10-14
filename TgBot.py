import telebot
from telebot import types
from background import keep_alive
from datetime import *

import Shedule


S_1251 = Shedule.Schedule_1251
S_1252 = Shedule.Schedule_1252

D = 'Понедельник'
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
F = ('{:%d %m %Y %H:%M:%S}'.format(datetime.now())).split()
B = datetime.strptime(f"{F[0]}-{F[1]}-{F[2]} {F[3]}", "%d-%m-%Y %H:%M:%S")
day = days[B.weekday()]

bot = telebot.TeleBot('7522385279:AAFqYqD3ukQ9ANrHixFSh6weeSCJZ--55_Y')

Spec_D = 0

def time():
    global D

    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    s = ('{:%d %m %Y %H:%M:%S}'.format(datetime.now())).split()

    d = datetime.strptime(f"{s[0]}-{s[1]}-{s[2]} {s[3]}", "%d-%m-%Y %H:%M:%S")

    Day = days[d.weekday()]

    c = 1
    ch = 1
    if c == 7:
        if ch == 1:
            ch = 0
            c = 0
        else:
            ch = 1
            c = 0

    if days[d.weekday()] != D:
        for i in range(len(days)):
            if D == days[i]:
                continue

            if Day == D:
                break
            D = days[i]
            c += 1

    now_data = ('{:%d %B}'.format(datetime.now()))
    return Day, now_data, ch

@bot.message_handler(commands=["start"])
def start(message):
    time()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет!")
    markup.add(btn1)

    bot.send_message(message.from_user.id, "👋 Привет! Я помогу тебе с расписанием!",
                     reply_markup=markup)



@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    global Spec_D
    Day, now_data, ch = time()
    if message.text == "👋 Привет!":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnD = types.KeyboardButton("Сегодня")
        btnR = types.KeyboardButton("Другой день")
        btnW = types.KeyboardButton("Эта неделя")
        btnRW = types.KeyboardButton("Следующая неделя")
        btn3 = types.KeyboardButton('Ошибка')
        markup.add(btnD, btnR, btnW, btnRW, btn3)
        bot.send_message(message.from_user.id, "На какой день Вы хотите узнать расписание?", reply_markup=markup)

    elif message.text == "1251":
        if Spec_D == 0:
            bot.send_message(message.from_user.id, f"{Day}, {now_data}  \n{S_1251[Day][ch]}")
        elif Spec_D == 1:
            bot.send_message(message.from_user.id, f"Понедельник \n{S_1251['Понедельник'][ch]} \n Вторник \n{S_1251['Вторник'][ch]} \n"
                                                   f"Среда \n {S_1251['Среда'][ch]} \n Четверг \n {S_1251['Четверг'][ch]} \n"
                                                   f"Пятница \n {S_1251['Пятница'][ch]} \n Суббота \n {S_1251['Суббота'][ch]} \n")

        elif Spec_D == 2:
            if ch == 0:
                bot.send_message(message.from_user.id,
                                 f"Понедельник \n{S_1251['Понедельник'][1]} \n Вторник \n{S_1251['Вторник'][1]} \n"
                                 f"Среда \n {S_1251['Среда'][1]} \n Четверг \n {S_1251['Четверг'][1]} \n"
                                 f"Пятница \n {S_1251['Пятница'][1]} \n Суббота \n {S_1251['Суббота'][1]} \n")
            else:
                bot.send_message(message.from_user.id,
                                 f"Понедельник \n{S_1251['Понедельник'][0]} \n Вторник \n{S_1251['Вторник'][0]} \n"
                                 f"Среда \n {S_1251['Среда'][0]} \n Четверг \n {S_1251['Четверг'][0]} \n"
                                 f"Пятница \n {S_1251['Пятница'][0]} \n Суббота \n {S_1251['Суббота'][0]} \n")

        else:
            bot.send_message(message.from_user.id, f"{Spec_D} \n {S_1251[Spec_D][ch]}")
    elif message.text == '1252':
        if Spec_D == 0:
            bot.send_message(message.from_user.id, f"{Day}, {now_data}  \n{S_1252[Day][ch]}")
        elif Spec_D == 1:
            bot.send_message(message.from_user.id,
                             f"Понедельник \n{S_1252['Понедельник'][ch]} \n Вторник \n{S_1252['Вторник'][ch]} \n"
                             f"Среда \n {S_1252['Среда'][ch]} \n Четверг \n {S_1252['Четверг'][ch]} \n"
                             f"Пятница \n {S_1252['Пятница'][ch]} \n Суббота \n {S_1252['Суббота'][ch]} \n")
        elif Spec_D == 2:
            if ch == 0:
                bot.send_message(message.from_user.id,
                                 f"Понедельник \n{S_1252['Понедельник'][1]} \n Вторник \n{S_1252['Вторник'][1]} \n"
                                 f"Среда \n {S_1252['Среда'][1]} \n Четверг \n {S_1252['Четверг'][1]} \n"
                                 f"Пятница \n {S_1252['Пятница'][1]} \n Суббота \n {S_1252['Суббота'][1]} \n")
            else:
                bot.send_message(message.from_user.id,
                                 f"Понедельник \n{S_1252['Понедельник'][0]} \n Вторник \n{S_1252['Вторник'][0]} \n"
                                 f"Среда \n {S_1252['Среда'][0]} \n Четверг \n {S_1252['Четверг'][0]} \n"
                                 f"Пятница \n {S_1252['Пятница'][0]} \n Суббота \n {S_1252['Суббота'][0]} \n")
        else:
            bot.send_message(message.from_user.id, f"{S_1252[Spec_D][ch]}")

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnD = types.KeyboardButton("Сегодня")
        btnR = types.KeyboardButton("Другой день")
        btnW = types.KeyboardButton("Эта неделя")
        btnRW = types.KeyboardButton("Следующая неделя")
        btn3 = types.KeyboardButton('Ошибка')
        markup.add(btnD, btnR, btnW, btnRW, btn3)
        bot.send_message(message.from_user.id, "На какой день Вы хотите узнать расписание?", reply_markup=markup)

    elif message.text in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]:
        Spec_D = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1251')
        btn2 = types.KeyboardButton("1252")
        btn_Ex = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn_Ex)
        bot.send_message(message.from_user.id, "Выберете свою группу", reply_markup=markup)

    elif message.text == 'Сегодня':
        Spec_D = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1251')
        btn2 = types.KeyboardButton("1252")
        btn_Ex = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn_Ex)
        bot.send_message(message.from_user.id, "Выберете свою группу", reply_markup=markup)

    elif message.text == 'Другой день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_M = types.KeyboardButton('Понедельник')
        btn_T = types.KeyboardButton('Вторник')
        btn_W = types.KeyboardButton('Среда')
        btn_Th = types.KeyboardButton('Четверг')
        btn_F = types.KeyboardButton('Пятница')
        btn_S = types.KeyboardButton('Суббота')
        btn_Ex = types.KeyboardButton('Назад')
        markup.add(btn_M, btn_T, btn_W, btn_Th, btn_F, btn_S, btn_Ex)
        bot.send_message(message.from_user.id, "Выберете день", reply_markup=markup)

    elif message.text=='Эта неделя':
        Spec_D = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1251')
        btn2 = types.KeyboardButton("1252")
        btn_Ex = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn_Ex)
        bot.send_message(message.from_user.id, "Выберете свою группу", reply_markup=markup)

    elif message.text=='Следующая неделя':
        Spec_D = 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('1251')
        btn2 = types.KeyboardButton("1252")
        btn_Ex = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn_Ex)
        bot.send_message(message.from_user.id, "Выберете свою группу", reply_markup=markup)


    elif message.text == 'Ошибка':
        bot.send_message(message.from_user.id, "Написать про ошибки бота или неправильное расписание можно" + " [сюда](https://t.me/Gha2347)", parse_mode="Markdown")




keep_alive()

bot.polling(none_stop=True, interval=0)
