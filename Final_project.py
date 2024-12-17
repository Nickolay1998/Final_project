import telebot
from telebot import types
from Translation import ru, eng, uk
bot = telebot.TeleBot("7705597030:AAGr4RzRzkr9YVi6SxxE1gpQfsnwSmUN6bA")
@bot.message_handler(commands=["start"])
def Languages(message):
    global markup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonru = types.KeyboardButton("Русский")
    buttonuk = types.KeyboardButton("Українська")
    buttoneng = types.KeyboardButton("English")
    buttonexit = types.KeyboardButton("Exit")
    markup.add(buttonru, buttonuk, buttoneng, buttonexit)
    bot.send_message(message.chat.id,"Choose language",reply_markup=markup)
    bot.register_next_step_handler(message, choose_language)
def choose_language(message):
    if message.text == "Русский":
        Start_Rus(message)
    elif message.text == "Українська":
        Start_Ukr(message)
    elif message.text == "English":
        Start_Eng(message)
    elif message.text == "Exit":
        Сancel(message)
    else:
        bot.send_message(message.chat.id, "Error",reply_markup=markup)
        bot.register_next_step_handler(message,choose_language)
def Сancel(message):
    bot.send_message(message.chat.id, "The program has stopped press /start to run the program.")
    bot.clear_step_handler_by_chat_id(message.chat.id)

##Russian version
def Start_Rus(message):
    bot.send_message(message.chat.id, ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id, ru.back)
    bot.send_message(message.chat.id, ru.new_light)
    bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)
def Сancel_Rus(message):
    bot.send_message(message.chat.id, ru.stop)
    bot.clear_step_handler_by_chat_id(message.chat.id)
##ButtonsRus
def keyboard_Rus():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    stop_b = types.KeyboardButton("Стоп")
    back_b = types.KeyboardButton("Назад")
    markup.add(stop_b, back_b)
    return markup

def button_Rus():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    b_yes = types.KeyboardButton("Да")
    b_no = types.KeyboardButton("Нет")
    back_b = types.KeyboardButton("Назад")
    markup.add(b_yes, b_no,back_b)
    return markup
#BackfuncRus______________
def back_this_month_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    Start_Rus(message)

def back_past_month_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id,ru.back)
    bot.send_message(message.chat.id,ru.old_light)
    bot.register_next_step_handler(message, Light_readings_for_the_past_month_Rus)

def water_this_month_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id,ru.back)
    bot.send_message(message.chat.id,ru.new_water)
    bot.register_next_step_handler(message, Water_readings_for_this_month_Rus)

def water_last_month_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id,ru.back)
    bot.send_message(message.chat.id,ru.old_water)
    bot.register_next_step_handler(message, Water_readings_for_last_month_Rus)

def back_kilowatts_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id,ru.back)
    bot.send_message(message.chat.id,ru.kl)
    bot.register_next_step_handler(message, Kilowatts_Rus)

def back_kub_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id,ru.back)
    bot.send_message(message.chat.id,ru.kb)
    bot.register_next_step_handler(message, Cubometers_Rus)

def trush_back_Rus(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
    bot.send_message(message.chat.id,ru.back)
    bot.send_message(message.chat.id,ru.tr)
    bot.register_next_step_handler(message, Trush_Rus)
##_________________________________________________________

def Light_readings_for_this_month_Rus(message):
     if message.text == "Стоп":
        Сancel_Rus(message)
        return
     elif message.text == "Назад":
        Languages(message)
        return
     try:
        global x
        x = int(message.text)
        if len(str(x)) == 5 and x>0:
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.old_light)
            bot.register_next_step_handler(message,Light_readings_for_the_past_month_Rus)
        else:
            if len(str(x)) < 5 or len(str(x)) > 5 or x<0:
                bot.send_message(message.chat.id,ru.error_five_num)
            bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.new_light)
     except ValueError:
        bot.send_message(message.chat.id,ru.error_num)
        bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.new_light)

def Light_readings_for_the_past_month_Rus(message):
    if message.text == "Стоп":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        back_this_month_Rus(message)
        return
    try:
        global y
        y = int(message.text)
        if len(str(y)) == 5 and y < x and y>0  or y==x:
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.new_water)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Rus)
        else:
            if len(str(y)) < 5 or len(str(y)) > 5 or y<0:
                bot.send_message(message.chat.id,ru.error_five_num)
            else:
                bot.send_message(message.chat.id,ru.error_last_num)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Rus)
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.old_light)
    except ValueError:
        bot.send_message(message.chat.id,ru.error_num)
        bot.register_next_step_handler(message, Light_readings_for_the_past_month_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.old_light)

def Water_readings_for_this_month_Rus(message):
    if message.text == "Стоп":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        back_past_month_Rus(message)
        return
    try:
        global p
        p = int(message.text)
        if len(str(p)) == 3 and p>0:
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.old_water)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Rus)
        else:
            if len(str(p)) < 3 or len(str(p)) > 3 or p<0:
                bot.send_message(message.chat.id,ru.error_three_num)
                bot.register_next_step_handler(message,Water_readings_for_this_month_Rus)
                bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
                bot.send_message(message.chat.id,ru.back)
                bot.send_message(message.chat.id,ru.new_water)
    except ValueError:
        bot.send_message(message.chat.id,ru.error_num)
        bot.register_next_step_handler(message, Water_readings_for_this_month_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.new_water)

def Water_readings_for_last_month_Rus(message):
    if message.text == "Стоп":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        water_this_month_Rus(message)
        return
    try:
        global k
        k = int(message.text)
        if len(str(k)) == 3 and k>0 and k < p or k==p:
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.kl)
            bot.register_next_step_handler(message, Kilowatts_Rus)
        else:
            if len(str(k)) < 3 or len(str(k)) > 3 or k<0:
                bot.send_message(message.chat.id,ru.error_three_num)
            else:
                bot.send_message(message.chat.id,ru.error_last_num)
            bot.register_next_step_handler(message,Water_readings_for_last_month_Rus)
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.old_water)
    except ValueError:
        bot.send_message(message.chat.id,ru.error_num)
        bot.register_next_step_handler(message,Water_readings_for_last_month_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.old_water)

def Kilowatts_Rus(message):
    if message.text == "Стоп":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        water_last_month_Rus(message)
        return
    try:
        global n
        n = float(message.text)
        if n > 0:
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.kb)
            bot.register_next_step_handler(message,Cubometers_Rus)
        else:
            bot.send_message(message.chat.id,ru.negative)
            bot.register_next_step_handler(message,Kilowatts_Rus)
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.kl)
    except ValueError:
        bot.send_message(message.chat.id,ru.error)
        bot.register_next_step_handler(message,Kilowatts_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.kl)

def Cubometers_Rus(message):
    if message.text == "Стоп":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        back_kilowatts_Rus(message)
        return
    try:
        global u
        u = float(message.text)
        if u>0:
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.tr)
            bot.register_next_step_handler(message,Trush_Rus)
        else:
            bot.send_message(message.chat.id,ru.negative)
            bot.register_next_step_handler(message,Cubometers_Rus)
            bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.back)
            bot.send_message(message.chat.id,ru.kb)
    except ValueError:
        bot.send_message(message.chat.id,ru.error)
        bot.register_next_step_handler(message,Cubometers_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.kb )

def Trush_Rus(message):
    if message.text == "Стоп":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        back_kub_Rus(message)
        return
    try:
        global trush
        trush = int(message.text)
        if trush > 0:
            bot.send_message(message.chat.id, f"{ru.new_light} {x} киловатт.")
            bot.send_message(message.chat.id, f"{ru.old_light} {y} киловатт.")
            bot.send_message(message.chat.id, f"{ru.new_water} {p} кубометров.")
            bot.send_message(message.chat.id, f"{ru.old_water} {k} кубометров.")
            bot.send_message(message.chat.id, f"{ru.kl} {n} Грн.")
            bot.send_message(message.chat.id, f"{ru.kb} {u}. Грн.")
            bot.send_message(message.chat.id, f"{ru.tr} {trush} Грн.")
            bot.send_message(message.chat.id, ru.back)
            bot.send_message(message.chat.id,ru.report,reply_markup=button_Rus())
            bot.register_next_step_handler(message, Order_Rus)
        else:
            bot.send_message(message.chat.id,ru.negative)
            bot.register_next_step_handler(message,Trush_Rus)
            bot.send_message(message.chat.id,ru.st)
            bot.send_message(message.chat.id,ru.back, reply_markup=keyboard_Rus())
            bot.send_message(message.chat.id,ru.tr)
    except ValueError:
        bot.send_message(message.chat.id,ru.error)
        bot.register_next_step_handler(message,Trush_Rus)
        bot.send_message(message.chat.id,ru.st,reply_markup=keyboard_Rus())
        bot.send_message(message.chat.id,ru.back)
        bot.send_message(message.chat.id,ru.tr)

def Order_Rus(message):
    if message.text == "Да":
        Сalculations_light_Rus(message)
        return
    elif message.text == "Нет":
        Сancel_Rus(message)
        return
    elif message.text == "Назад":
        trush_back_Rus(message)
        return
    else:
        bot.send_message(message.chat.id,ru.ec,reply_markup=button_Rus())
        bot.register_next_step_handler(message,Order_Rus)

def Сalculations_light_Rus(message):
    global light
    light = (x - y) * n
    Сalculations_water_Rus(message)

def Сalculations_water_Rus(message):
    global water
    water = (p - k) * u
    Сalculations_summ_Rus(message)

def Сalculations_summ_Rus(message):
    global summ
    summ = round(light, 1) + round(water, 1) + round(trush, 1)
    results_table_Rus(message)

def results_table_Rus(message):
    bot.send_message(message.chat.id, f"Свет: {x}-{y} = {x-y} Квт.")
    bot.send_message(message.chat.id, f"Вода: {p}-{k} = {p-k} Кбм.")
    bot.send_message(message.chat.id, f"Мусор: {round(trush, 1)} Грн.")
    bot.send_message(message.chat.id, f"{x-y}*{n} = {round(light, 1)} Грн.")
    bot.send_message(message.chat.id, f"{p-k}*{u} = {round(water, 1)} Грн.")
    bot.send_message(message.chat.id,f"Сумма за коммунальные услуги: {round(light, 1)} + {round(water, 1)} + {round(trush, 1)} = {round(summ, 1)} Грн.")
    bot.send_message(message.chat.id, "Нажмите /start для запуска.")

## Ukraine version
#ButtonUkr_________________
def keyboard_Ukr():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    stop_b = types.KeyboardButton("Стоп")
    back_b = types.KeyboardButton("Назад")
    markup.add(stop_b, back_b)
    return markup

def button_Ukr():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    b_yes = types.KeyboardButton("Так")
    b_no = types.KeyboardButton("Ні")
    back_b = types.KeyboardButton("Назад")
    markup.add(b_yes, b_no,back_b)
    return markup
#BackfunkUkr____________________
def back_this_month_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    Start_Ukr(message)

def back_past_month_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.old_light)
    bot.register_next_step_handler(message,Light_readings_for_the_past_month_Ukr)

def water_this_month_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.new_water)
    bot.register_next_step_handler(message,Water_readings_for_this_month_Ukr)

def water_last_month_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.old_water)
    bot.register_next_step_handler(message,Water_readings_for_last_month_Ukr)

def back_kilowatts_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.kl)
    bot.register_next_step_handler(message,Kilowatts_Ukr)

def back_kub_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.kb)
    bot.register_next_step_handler(message,Cubometers_Ukr)

def trush_back_Ukr(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.tr)
    bot.register_next_step_handler(message,Trush_Ukr)
#_____________________________________________________________

def Start_Ukr(message):
    bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
    bot.send_message(message.chat.id,uk.back)
    bot.send_message(message.chat.id,uk.new_light)
    bot.register_next_step_handler(message,Light_readings_for_this_month_Ukr)

def Сancel_Ukr(message):
    bot.send_message(message.chat.id,uk.stop)
    bot.clear_step_handler_by_chat_id(message.chat.id)

def Light_readings_for_this_month_Ukr(message):
     if message.text == "Стоп":
        Сancel_Ukr(message)
        return
     elif message.text == "Назад":
        Languages(message)
        return
     try:
        global x
        x = int(message.text)
        if len(str(x)) == 5 and x>0:
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.old_light)
            bot.register_next_step_handler(message,Light_readings_for_the_past_month_Ukr)
        else:
            if len(str(x)) < 5 or len(str(x)) > 5 or x<0:
                bot.send_message(message.chat.id,uk.error_five_num)
                bot.register_next_step_handler(message,Light_readings_for_this_month_Ukr)
                bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
                bot.send_message(message.chat.id,uk.back)
                bot.send_message(message.chat.id,uk.new_light)
     except ValueError:
        bot.send_message(message.chat.id,uk.error_num)
        bot.register_next_step_handler(message,Light_readings_for_this_month_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.new_light)

def Light_readings_for_the_past_month_Ukr(message):
    if message.text == "Стоп":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        back_this_month_Ukr(message)
        return
    try:
        global y
        y = int(message.text)
        if len(str(y)) == 5 and y < x or y==x and y>0:
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.new_water)
            bot.register_next_step_handler(message,Water_readings_for_this_month_Ukr)
        else:
            if len(str(y)) < 5 or len(str(y)) > 5 or y<0:
                bot.send_message(message.chat.id,uk.error_five_num)
            else:
                bot.send_message(message.chat.id,uk.error_last_num)
            bot.register_next_step_handler(message,Light_readings_for_the_past_month_Ukr)
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.old_light)
    except ValueError:
        bot.send_message(message.chat.id,uk.error_num)
        bot.register_next_step_handler(message,Light_readings_for_the_past_month_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.old_light)

def Water_readings_for_this_month_Ukr(message):
    if message.text == "Стоп":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        back_past_month_Ukr(message)
        return
    try:
        global p
        p = int(message.text)
        if len(str(p)) == 3 and p>0:
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.old_water)
            bot.register_next_step_handler(message,Water_readings_for_last_month_Ukr)
        else:
            if len(str(p)) < 3 or len(str(p)) > 3 or p<0:
                bot.send_message(message.chat.id,uk.error_three_num)
                bot.register_next_step_handler(message,Water_readings_for_this_month_Ukr)
                bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
                bot.send_message(message.chat.id,uk.back)
                bot.send_message(message.chat.id,uk.new_water)
    except ValueError:
        bot.send_message(message.chat.id,uk.error_num)
        bot.register_next_step_handler(message,Water_readings_for_this_month_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.new_water)

def Water_readings_for_last_month_Ukr(message):
    if message.text == "Стоп":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        water_this_month_Ukr(message)
        return
    try:
        global k
        k = int(message.text)
        if len(str(k)) == 3 and k>0 and k < p or k==p:
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.kl)
            bot.register_next_step_handler(message,Kilowatts_Ukr)
        else:
            if len(str(k)) < 3 or len(str(k)) > 3 or k<0:
                bot.send_message(message.chat.id,uk.error_three_num)
            else:
                bot.send_message(message.chat.id,uk.error_last_num)
            bot.register_next_step_handler(message,Water_readings_for_last_month_Ukr)
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.old_water)
    except ValueError:
        bot.send_message(message.chat.id,uk.error_num)
        bot.register_next_step_handler(message,Water_readings_for_last_month_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.old_water)

def Kilowatts_Ukr(message):
    if message.text == "Стоп":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        water_last_month_Ukr(message)
        return
    try:
        global n
        n = float(message.text)
        if n>0:
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.kb)
            bot.register_next_step_handler(message,Cubometers_Ukr)
        else:
            bot.send_message(message.chat.id,uk.negative)
            bot.register_next_step_handler(message,Kilowatts_Ukr)
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.kl)
    except ValueError:
        bot.send_message(message.chat.id,uk.error)
        bot.register_next_step_handler(message,Kilowatts_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.kl)

def Cubometers_Ukr(message):
    if message.text == "Стоп":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        back_kilowatts_Ukr(message)
        return
    try:
        global u
        u = float(message.text)
        if u > 0:
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.tr)
            bot.register_next_step_handler(message,Trush_Ukr)
        else:
            bot.send_message(message.chat.id,uk.negative)
            bot.register_next_step_handler(message,Cubometers_Ukr)
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.kb)

    except ValueError:
        bot.send_message(message.chat.id,uk.error)
        bot.register_next_step_handler(message,Cubometers_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.kb )

def Trush_Ukr(message):
    if message.text == "Стоп":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        back_kub_Ukr(message)
        return
    try:
        global trush
        trush = int(message.text)
        if trush > 0:
            bot.send_message(message.chat.id, f"{uk.new_light} {x} кіловат.")
            bot.send_message(message.chat.id, f"{uk.old_light} {y} кіловат.")
            bot.send_message(message.chat.id, f"{uk.new_water} {p} кубометрів.")
            bot.send_message(message.chat.id, f"{uk.old_water} {k} кубометрів.")
            bot.send_message(message.chat.id, f"{uk.kl} {n} Грн.")
            bot.send_message(message.chat.id, f"{uk.kb} {u} Грн.")
            bot.send_message(message.chat.id, f"{uk.tr} {trush} Грн.")
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.report,reply_markup=button_Ukr())
            bot.register_next_step_handler(message,Order_Ukr)
        else:
            bot.send_message(message.chat.id,uk.negative)
            bot.register_next_step_handler(message,Trush_Ukr)
            bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
            bot.send_message(message.chat.id,uk.back)
            bot.send_message(message.chat.id,uk.tr)
    except ValueError:
        bot.send_message(message.chat.id,uk.error)
        bot.register_next_step_handler(message,Trush_Ukr)
        bot.send_message(message.chat.id,uk.st,reply_markup=keyboard_Ukr())
        bot.send_message(message.chat.id,uk.back)
        bot.send_message(message.chat.id,uk.tr)

def Order_Ukr(message):
    if message.text == "Так":
        Сalculations_light_Ukr(message)
        return
    elif message.text == "Ні":
        Сancel_Ukr(message)
        return
    elif message.text == "Назад":
        trush_back_Ukr(message)
        return
    else:
        bot.send_message(message.chat.id,uk.ec,reply_markup=button_Ukr())
        bot.register_next_step_handler(message,Order_Ukr)

def Сalculations_light_Ukr(message):
    global light
    light = (x - y) * n
    Сalculations_water_Ukr(message)

def Сalculations_water_Ukr(message):
    global water
    water = (p - k) * u
    Сalculations_summ_Ukr(message)

def Сalculations_summ_Ukr(message):
    global summ
    summ = round(light,1) + round(water,1) + round(trush,1)
    results_table_Ukr(message)

def results_table_Ukr(message):
    bot.send_message(message.chat.id, f"Світло: {x}-{y} = {x-y} Квт.")
    bot.send_message(message.chat.id, f"Вода: {p}-{k} = {p-k} Кбм.")
    bot.send_message(message.chat.id, f"Сміття: {round(trush,1)} Грн.")
    bot.send_message(message.chat.id, f"{x-y}*{n} = {round(light,1)} Грн.")
    bot.send_message(message.chat.id, f"{p-k}*{u} = {round(water,1)} Грн.")
    bot.send_message(message.chat.id, f"Сума за комунальні послуги: {round(light,1)} + {round(water,1)} + {round(trush,1)} = {round(summ, 1)} Грн.")
    bot.send_message(message.chat.id,f"Натисніть /start для запуску.")
##English version
##ButtomEng________________
def keyboard_Eng():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    stop_b = types.KeyboardButton("Stop")
    back_b = types.KeyboardButton("Back")
    markup.add(stop_b, back_b)
    return markup

def button_Eng():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    b_yes = types.KeyboardButton("Yes")
    b_no = types.KeyboardButton("No")
    back_b = types.KeyboardButton("Back")
    markup.add(b_yes, b_no, back_b)
    return markup
##_____________________________

#Backfunc___________________________
def back_this_month_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    Start_Eng(message)

def back_past_month_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.old_light)
    bot.register_next_step_handler(message,Light_readings_for_the_past_month_Eng)

def water_this_month_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.new_water)
    bot.register_next_step_handler(message,Water_readings_for_this_month_Eng)

def water_last_month_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.old_water)
    bot.register_next_step_handler(message,Water_readings_for_last_month_Eng)

def back_kilowatts_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.kl)
    bot.register_next_step_handler(message,Kilowatts_Eng)

def back_kub_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.kb)
    bot.register_next_step_handler(message,Cubometers_Eng)

def trush_back_Eng(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.tr)
    bot.register_next_step_handler(message,Trush_Eng)
##__________________________________________________________
def Start_Eng(message):
    bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
    bot.send_message(message.chat.id,eng.back)
    bot.send_message(message.chat.id,eng.new_light)
    bot.register_next_step_handler(message,Light_readings_for_this_month_Eng)

def Сancel_Eng(message):
    bot.send_message(message.chat.id,eng.stop)
    bot.clear_step_handler_by_chat_id(message.chat.id)

def Light_readings_for_this_month_Eng(message):
     if message.text == "Stop":
        Сancel_Eng(message)
        return
     elif message.text == "Back":
        Languages(message)
        return
     try:
        global x
        x = int(message.text)
        if len(str(x)) == 5 and x>0:
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.old_light)
            bot.register_next_step_handler(message,Light_readings_for_the_past_month_Eng)
        else:
            if len(str(x)) < 5 or len(str(x)) > 5 or x<5:
                bot.send_message(message.chat.id,eng.error_five_num)
                bot.register_next_step_handler(message,Light_readings_for_this_month_Eng)
                bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
                bot.send_message(message.chat.id,eng.back)
                bot.send_message(message.chat.id,eng.new_light)
     except ValueError:
        bot.send_message(message.chat.id,eng.error_num)
        bot.register_next_step_handler(message,Light_readings_for_this_month_Eng)
        bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.new_light)

def Light_readings_for_the_past_month_Eng(message):
    if message.text == "Stop":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        back_this_month_Eng(message)
        return
    try:
        global y
        y = int(message.text)
        if len(str(y)) == 5 and y < x or y==x and y>0:
            bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.new_water)
            bot.register_next_step_handler(message,Water_readings_for_this_month_Eng)
        else:
            if len(str(y)) < 5 or len(str(y)) > 5 or y<0:
                bot.send_message(message.chat.id,eng.error_five_num)
            else:
                bot.send_message(message.chat.id,eng.error_last_num)
            bot.register_next_step_handler(message,Light_readings_for_the_past_month_Eng)
            bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.old_light)
    except ValueError:
        bot.send_message(message.chat.id,eng.error_num)
        bot.register_next_step_handler(message,Light_readings_for_the_past_month_Eng)
        bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.old_light)

def Water_readings_for_this_month_Eng(message):
    if message.text == "Stop":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        back_past_month_Eng(message)
        return
    try:
        global p
        p = int(message.text)
        if len(str(p)) == 3 and p>0:
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.old_water)
            bot.register_next_step_handler(message,Water_readings_for_last_month_Eng)
        else:
            if len(str(p)) < 3 or len(str(p)) > 3 or p<0:
                bot.send_message(message.chat.id,eng.error_three_num)
                bot.register_next_step_handler(message,Water_readings_for_this_month_Eng)
                bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
                bot.send_message(message.chat.id,eng.back)
                bot.send_message(message.chat.id,eng.new_water)
    except ValueError:
        bot.send_message(message.chat.id,eng.error_num)
        bot.register_next_step_handler(message,Water_readings_for_this_month_Eng)
        bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.new_water)

def Water_readings_for_last_month_Eng(message):
    if message.text == "Stop":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        water_this_month_Eng(message)
        return
    try:
        global k
        k = int(message.text)
        if len(str(k)) == 3 and k < p or k==p and k>0:
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.kl)
            bot.register_next_step_handler(message,Kilowatts_Eng)
        else:
            if len(str(k)) < 3 or len(str(k)) > 3 or k<0:
                bot.send_message(message.chat.id,eng.error_three_num)
            else:
                bot.send_message(message.chat.id,eng.error_last_num)
            bot.register_next_step_handler(message,Water_readings_for_last_month_Eng)
            bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.old_water)
    except ValueError:
        bot.send_message(message.chat.id,eng.error_num)
        bot.register_next_step_handler(message,Water_readings_for_last_month_Eng)
        bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.old_water)

def Kilowatts_Eng(message):
    if message.text == "Stop":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        water_last_month_Eng(message)
        return
    try:
        global n
        n = float(message.text)
        if n>0:
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.kb)
            bot.register_next_step_handler(message,Cubometers_Eng)
        else:
            bot.send_message(message.chat.id,eng.negative)
            bot.register_next_step_handler(message,Kilowatts_Eng)
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.kl)
    except ValueError:
        bot.send_message(message.chat.id,eng.error)
        bot.register_next_step_handler(message,Kilowatts_Eng)
        bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.kl)

def Cubometers_Eng(message):
    if message.text == "Stop":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        back_kilowatts_Eng(message)
        return
    try:
        global u
        u = float(message.text)
        if u>0:
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.tr)
            bot.register_next_step_handler(message,Trush_Eng)
        else:
            bot.send_message(message.chat.id,eng.negative)
            bot.register_next_step_handler(message,Cubometers_Eng)
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.kb)
    except ValueError:
        bot.send_message(message.chat.id,eng.error)
        bot.register_next_step_handler(message,Cubometers_Eng)
        bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.kb )

def Trush_Eng(message):
    if message.text == "Stop":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        back_kub_Eng(message)
        return
    try:
        global trush
        trush = int(message.text)
        if trush>0:
            bot.send_message(message.chat.id, f"{eng.new_light} {x} kilowatts.")
            bot.send_message(message.chat.id, f"{eng.old_light} {y} kilowatts.")
            bot.send_message(message.chat.id, f"{eng.new_water} {p} cubic meters.")
            bot.send_message(message.chat.id, f"{eng.old_water} {k} cubic meters.")
            bot.send_message(message.chat.id, f"{eng.kl} {n} UAH.")
            bot.send_message(message.chat.id, f"{eng.kb} {u} UAH.")
            bot.send_message(message.chat.id, f"{eng.tr} {trush} UAH.")
            bot.send_message(message.chat.id, eng.back)
            bot.send_message(message.chat.id, eng.report, reply_markup=button_Eng())
            bot.register_next_step_handler(message, Order_Eng)
        else:
            bot.send_message(message.chat.id,eng.negative)
            bot.register_next_step_handler(message,Trush_Eng)
            bot.send_message(message.chat.id,eng.st, reply_markup=keyboard_Eng())
            bot.send_message(message.chat.id,eng.back)
            bot.send_message(message.chat.id,eng.tr)
    except ValueError:
        bot.send_message(message.chat.id,eng.error)
        bot.register_next_step_handler(message,Trush_Eng)
        bot.send_message(message.chat.id,eng.st,reply_markup=keyboard_Eng())
        bot.send_message(message.chat.id,eng.back)
        bot.send_message(message.chat.id,eng.tr)

def Order_Eng(message):
    if message.text == "Yes":
        Сalculations_light_Eng(message)
        return
    elif message.text == "No":
        Сancel_Eng(message)
        return
    elif message.text == "Back":
        trush_back_Eng(message)
        return
    else:
        bot.send_message(message.chat.id,eng.ec,reply_markup=button_Eng())
        bot.register_next_step_handler(message,Order_Eng)

def Сalculations_light_Eng(message):
    global light
    light = (x - y) * n
    Сalculations_water_Eng(message)

def Сalculations_water_Eng(message):
    global water
    water = (p - k) * u
    Сalculations_summ_Eng(message)

def Сalculations_summ_Eng(message):
    global summ
    summ = round(light,1) + round(water,1) + round(trush,1)
    results_table_Eng(message)

def results_table_Eng(message):
    bot.send_message(message.chat.id, f"Light: {x}-{y} = {x-y} Kwh")
    bot.send_message(message.chat.id, f"Water: {p}-{k} = {p-k} Kbm")
    bot.send_message(message.chat.id, f"Trash: {round(trush,1)} UAH.")
    bot.send_message(message.chat.id, f"{x-y}*{n} = {round(light,1)} UAH.")
    bot.send_message(message.chat.id, f"{p-k}*{u} = {round(water,1)} UAH.")
    bot.send_message(message.chat.id, f"Total utility costs: {round(light,1)} + {round(water,1)} + {round(trush,1)} = {round(summ, 1)} UAH.")
    bot.send_message(message.chat.id,f"Press /start for run")
bot.infinity_polling()


