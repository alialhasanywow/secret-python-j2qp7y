import telebot
import requests
from flask import Flask
from threading import Thread
from server import server


token = "6765941935:AAExwPMeWgZHP2okaEJuOvk58dMyPx5AyaM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """اهلا في بوت يرسل رسائل الي رقم حساب تليكرام عن طريق رقم الهاتف 📱 ! ارسل الان رقمك مع رمز الدوله بهذه الشكل 👇🏻 .
    مثال : 96411111111111+""")

    @bot.message_handler(func=lambda message: True)
    def verify_phone_number(message):
        try:
                phone = message.text
                        headers = {
                                    'bot_id': '1288099309',
                                                'origin': 'https://t.me',
                                                            'lang': 'en'
                                                                    }
                                                                            data = {
                                                                                        'phone': f'{phone}'
                                                                                                }
                                                                                                        response = requests.post('https://oauth.tg.dev/auth/request?bot_id=1288099309&origin=https://t.me&lang=en', headers=headers,data=data)
                                                                                                                bot.reply_to(message, 'تم ارسال الكود  !')
                                                                                                                    except Exception as e:
                                                                                                                            bot.reply_to(message, 'غير الرقم او ارسلة من جديد او الرقم غلط 📨 !')

                                                                                                                            app = Flask('')
                                                                                                                            @app.route('/')
                                                                                                                            def ping():
                                                                                                                                return "PONG !,IM AWAKE"

                                                                                                                                def run():
                                                                                                                                    app.run(host='0.0.0.0', port=8080)

                                                                                                                                    def server():
                                                                                                                                        t = Thread(target=run)
                                                                                                                                            t.start()
                                                                                                                                            server()
                                                                                                                                            bot.polling(none_stop=True)