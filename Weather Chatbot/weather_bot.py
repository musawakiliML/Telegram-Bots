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
updater.idle()
