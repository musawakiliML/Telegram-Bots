'''
import pyowm
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import logging


#enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)'
)

API_KEY = '1f044a70f0d3ab8c1377ff9aec5827c3'

def main_bot():
    updater = Updater('900246962:AAEYa-hb4z2sZfqzbB2eNSKBLozBB_qzK70', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


    updater.start_polling()


    updater.idle()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi!")
def help_command(update: Update, context:CallbackContext):
    update.message.reply_text("Help!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


main_bot()


def weather_func(place):

    own = pyowm.OWM(API_KEY)
    mgr = own.weather_manager()
    obs = mgr.weather_at_place(place)

    weather = obs.weather

    temperature = weather.temperature(unit='kelvin')['temp']
    
    return [temperature]

weather = weather_func("potiskum")

print(weather)
'''

import pyowm
from telegram.ext import CommandHandler, Updater

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def city_name():
    owm = pyowm.OWM(API_KEY)
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place('Bauchi')
    
    weather = obs.weather
    
    temperature = weather.temperature(unit='fahrenheit')['temp']
    
    result = f"The temperature is {temperature}"
    
    return result

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def get_weather(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text=city_name())

get_weather_handler = CommandHandler("getweather", get_weather)
dispatcher.add_handler(get_weather_handler)

updater.start_polling()