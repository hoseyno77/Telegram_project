import telebot
import base2


bot = telebot.TeleBot(base2.TOKEN)

print("bat created...")

@bot.message_handler(commands=['start'])
def say_hello(massage):
    bot.send_message(massage.chat.id, 
    text= """سلام! 👋
به ربات تبریک روز برنامه‌نویس خوش آمدید.

این ربات برای تشکر از استاد عزیزمان ساخته شده است. 💙🐍
""")

@bot.message_handler(commands= ["help"])
def show_help_msg(message):
    bot.reply_to(message,text="برای دیدن پیام‌ها وتبریکات /menu انتخاب کنید🌸")



@bot.message_handler(commands=['menu'])    
def show_menu(message):
    print(message)
    markup = telebot.types.ReplyKeyboardMarkup()
    
    btn1 = telebot.types.KeyboardButton(text='🎁 پیام تبریک برای استاد')
    btn2 = telebot.types.KeyboardButton(text='🐍 تبریک به زبان Python')

    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, 'یکی از گزینه های زیر را انتخاب کنید ', reply_markup=markup)



@bot.message_handler(func=lambda message:True)
def handle_all_messages(message):
    if message.text == ('🎁 پیام تبریک برای استاد'):
        info = """🎉 روز برنامه‌نویس مبارک، استاد عزیز! 💙

شاید امروز بتوانیم با چند خط کد
یک ربات بسازیم، اما پشت هر خط کدی
که یاد گرفته‌ایم، زحمات و آموزش‌های
ارزشمند شماست.

ممنون که مسیر یادگیری برنامه‌نویسی
را برای ما روشن کردید.
امیدواریم روزی برسد که با مهارت‌هایی
که از شما آموخته‌ایم، پروژه‌های بزرگی
بسازیم.

با احترام و سپاس فراوان
از طرف شاگردان شما 🌹
"""


        bot.send_message(message.chat.id, text=info)

    elif message.text == '🐍 تبریک به زبان Python':
        bot.send_message(message.chat.id, text = """
teacher = "استاد عزیز"

print("روز برنامه‌نویس مبارک!")
print("ممنون که کدنویسی را به ما آموختید.")
print("هر خط کدی که می‌نویسیم، یادگاری از شماست.")
""")

    


    else:
        bot.send_message(message.chat.id , 'منظور شما را متوجه نشدم! دوباره تلاش کنید')
        


  
if __name__ == '__main__':
    
    
    bot.infinity_polling()
