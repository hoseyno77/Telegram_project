import telebot
import base
import  app_api

bot = telebot.TeleBot(base.TOKEN)

print("bat created...")

@bot.message_handler(commands=['start'])
def say_hello(massage):
    bot.send_message(massage.chat.id, 
    text="به بات خانه نویسان خوش امدید")

@bot.message_handler(commands= ["help","support"])
def show_help_msg(message):
    bot.reply_to(message,text="در صورت نیاز با شماره 123 تماس بگیرید")

@bot.message_handler(commands=['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(text ="اخبار ورزشی",url='https://www.varzesh3.com')
    btn2 = telebot.types.InlineKeyboardButton(text ="اخبار  عمومی",url='https://www.tasnimnews.ir')
    btn3 = telebot.types.InlineKeyboardButton(text ="اخبار اقتصادی",url='https://tardingview.com')
    
    markup.add(btn1,btn2,btn3)

    bot.send_message(message.chat.id, 
    text='یکی از گزینه های زیر را انتخاب کنید ',reply_markup=markup)

@bot.message_handler(commands=['menu'])    
def show_menu(message):
    print(message)
    markup = telebot.types.ReplyKeyboardMarkup()
    
    btn1 = telebot.types.KeyboardButton(text='تماس با ما')
    btn2 = telebot.types.KeyboardButton(text='درباره ما')
    btn3 = telebot.types.KeyboardButton(text='تعیین عضویت')
    btn4= telebot.types.KeyboardButton(text='بازگشت')

    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id, 'یکی از گزینه های زیر را انتخاب کنید ', reply_markup=markup)


@bot.message_handler(commands=['movie'])
def show_message(message):
    msg = bot.send_message(message.chat.id,'ایدی فیلم مورد نطر را وارد کن')
    bot.register_next_step_handler(msg, get_movie_info)

def get_movie_info(message):
    movie_id = message.text
    result = app_api.get_movie_info_by_id(movie_id)
    bot.send_message(message.chat.id,text= f"{result[0]} / {result[-1]}")

@bot.message_handler(commands=['movie2'])
def show_message(message):
    msg = bot.send_message(message.chat.id,'اسم فیلم مورد نظر را بنویسید')
    bot.register_next_step_handler(msg,get_movie_info_name)    
     
def get_movie_info_name (message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    bot.send_message(message.chat.id,text = f'{result[1]}/{result[2]}')


@bot.message_handler(func=lambda message:True)
def handle_all_messages(message):
    if message.text == 'تماس با ما':
        email = 'support1545@gmail.com'
        phone = '09123651425'
        post_box = '23124563'
        info = f'ایمیل:{email} / شماره تماس: {phone} / صندوق پستی: {post_box}'

        bot.send_message(message.chat.id, text=info)

    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, text = ' یک گروه آموزشی با ایده هایی روشن و مشخص')

    elif message.text == 'تعیین عضویت':
        # membership_type = {'noraml':'3 ماهه' , 'vip':'یک ساله' , 'first class': 'نامحدود'}
        bot.send_message(message.chat.id , text='یکی از گزینه های 3 ماهه / یکساله و نامحدود ر انتخاب کنید')
    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text='به منوی اصلی باز گردید', reply_markup=markup)

    else:
        bot.send_message(message.chat.id , 'منظور شما را متوجه نشدم! دوباره تلاش کنید')
        


  
if __name__ == '__main__':
    
    
    bot.infinity_polling()
