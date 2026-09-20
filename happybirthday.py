import telebot
import base2

bot = telebot.TeleBot(base2.TOKEN)

print("birthday bot created...")


@bot.message_handler(commands=['start'])
def say_hello(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add("💌 پیام مامان")
    keyboard.add("🎁 سورپرایز تولد")
    keyboard.add("🌷 آرزوهای مامان")
    keyboard.add("❤️ دوستت دارم")

    bot.send_message(
        message.chat.id,
        text="🎂 تولدت مبارک دختر عزیزم ❤️\n\n"
             "برای دیدن پیام‌ها و سورپرایزها یکی از گزینه‌ها رو انتخاب کن 🌸",
        reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def show_help(message):

    bot.reply_to(
        message,
        text="از دکمه‌های پایین برای دیدن سورپرایزهای تولدت استفاده کن 🎁"
    )


@bot.message_handler(func=lambda message: message.text == "💌 پیام مامان")
def mother_message(message):

    bot.send_message(
        message.chat.id,
        text="💌 دختر عزیزم...\n\n"
             "تو یکی از قشنگ‌ترین هدیه‌های زندگی من هستی. "
             "امیدوارم همیشه دلت شاد و لبت خندون باشه. 🌷\n\n"
             "🎂 تولدت مبارک دختر قشنگم ❤️"
    )


@bot.message_handler(func=lambda message: message.text == "🎁 سورپرایز تولد")
def birthday_surprise(message):

    bot.send_message(
        message.chat.id,
        text="🎁 یه سورپرایز کوچولو برات دارم...\n\n"
             "✨ 3\n"
             "✨ 2\n"
             "✨ 1\n\n"
             "🎉تو بی نظیری🎂❤️"
    )


@bot.message_handler(func=lambda message: message.text == "🌷 آرزوهای مامان")
def mothers_wishes(message):

    bot.send_message(
        message.chat.id,
        text="🌷 آرزو می‌کنم...\n\n"
             "✨ همیشه سالم و شاد باشی\n"
             "✨ به آرزوهات برسی\n"
             "✨ همیشه لبخند روی لبت باشه\n"
             "✨ و زندگی برات پر از اتفاق‌های قشنگ باشه ❤️"
    )


@bot.message_handler(func=lambda message: message.text == "❤️ دوستت دارم")
def love_message(message):

    bot.send_message(
        message.chat.id,
        text="❤️ دوستت دارم دخترم.\n\n"
             "هیچ کلمه‌ای نمی‌تونه اندازه‌ی عشقی که بهت دارم رو بیان کنه. 🌸"
    )




bot.infinity_polling()