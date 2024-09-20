import telebot

TOKEN = "7086862785:AAHCB_BDJ3Ffly4gpcOVDFuWFX1LeBzf0rk"

WEBHOOK_URL = 'https://telbot-7kzz.onrender.com' + TOKEN

bot = telebot.TeleBot("7086862785:AAHCB_BDJ3Ffly4gpcOVDFuWFX1LeBzf0rk")


key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_markup.add("پرسشنامه")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , "سلام متقاضی گرامی \nبه ربات آیا شما ابله هستید؟ خوش آمدید" , reply_markup=key_markup)

@bot.message_handler(func= lambda message: message.text == "پرسشنامه")
def q1(message):
    q1m = bot.send_message(message.chat.id , "آیا شما عوضی هستید؟")
    bot.register_next_step_handler(q1m , q2)

def q2(message):
    user_data = {'q1': message.text}
    q2m = bot.send_message(message.chat.id , "آیا شما دیگران را اذیت می کنید؟")
    bot.register_next_step_handler(q2m , q3 , user_data)

def q3(message , user_data):
    user_data['q2'] = message.text
    q3m = bot.send_message(message.chat.id , "آیا شما دیگران را مسخره می کنید؟")
    bot.register_next_step_handler(q3m , end , user_data)

def end(message , user_data):
    number = 0
    user_data['q3'] = message.text
    #bot.send_message(message.chat.id , f"جواب شما به سوال ها {user_data['q1']}\n{user_data['q2']}\n{user_data['q3']}")
    if user_data['q1'] == 'بله':
        number += 1
    if user_data['q2'] == 'بله':
        number += 1
    if user_data['q3'] == 'بله':
        number += 1
    if number >= 2:
        bot.send_message(message.chat.id , "متاسفانه شما ابله هستید")
    else:
        bot.send_message(message.chat.id , "خوشبختانه شما ابله نیستید")

def setup_webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

if __name__ == "__main__":
    setup_webhook()
    
    # دریافت درخواست‌های Webhook از تلگرام
    bot.polling(none_stop=True)
