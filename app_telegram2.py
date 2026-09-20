import telebot
import base
import app_api2


bot = telebot.TeleBot(base.TOKEN)

print("bot created...")


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id,text=" به بات آب و هوای ما خوش آمدید")


@bot.message_handler(commands=["help"])
def show_help_msg(message):
    bot.reply_to(message,text="برای دریافت آب و هوا از دستور /weather استفاده کنید")

@bot.message_handler(commands=['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(" اخبار هواشناسی ایران",
        url="https://www.vista.ir/t/8/%D9%88%D8%B6%D8%B9%2B%D9%87%D9%88%D8%A7%DB%8C%2Bای%D8%B1%D8%A7%DB%8C%D8%A7%D9%86")
    btn2 = telebot.types.InlineKeyboardButton( "پیش‌بینی وضعیت آب‌وهوای ایران",
        url="https://www.skyweather.ir/")
    
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, 
    text='یکی از گزینه های زیر را انتخاب کنید ',reply_markup=markup)


@bot.message_handler(commands=['weather'])
def show_weather(message):
    msg = bot.send_message(message.chat.id,"اسم شهر مورد نظر را وارد کنید")

    bot.register_next_step_handler(msg,get_weather)

def get_weather(message):
    city = message.text
    result = app_api2.get_weather(city)
    bot.send_message(message.chat.id,text = f'دما:{result[1]}  \n سرعت وزش باد:{result[2]}')

    

@bot.message_handler(commands=['menu'])
def show_menu(message):
    print(message)

    markup = telebot.types.ReplyKeyboardMarkup()


    btn1 = telebot.types.KeyboardButton(text='آب و هوای امروز')
    btn2 = telebot.types.KeyboardButton(text='جستجوی شهر')
    btn3 = telebot.types.KeyboardButton(text='درباره ما')
    btn4 = telebot.types.KeyboardButton(text='بازگشت')

    markup.add(btn1, btn2,btn3, btn4)

    bot.send_message(message.chat.id,'یکی از گزینه‌های زیر را انتخاب کنید:',reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):

    if message.text == 'آب و هوای امروز':

        msg = bot.send_message(message.chat.id,'اسم شهر را وارد کنید')

        bot.register_next_step_handler(msg, get_weather)

    elif message.text == 'جستجوی شهر':

        msg = bot.send_message(message.chat.id,'اسم شهر مورد نظر را بنویسید')

        bot.register_next_step_handler(msg, get_weather)

    elif message.text == 'درباره ما':

        bot.send_message(message.chat.id,
        'این ربات برای نمایش اطلاعات آب و هوای شهرهای ایران ساخته شده است.')

    elif message.text == 'بازگشت':

        markup = telebot.types.ReplyKeyboardRemove()

        bot.send_message(message.chat.id,'به منوی اصلی بازگشتید',reply_markup=markup)

    else:

        bot.send_message(message.chat.id,'منظور شما را متوجه نشدم!')


if __name__ == '__main__':

    bot.infinity_polling()