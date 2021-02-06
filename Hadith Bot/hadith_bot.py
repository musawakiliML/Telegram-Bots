import requests
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

updater = Updater(token="1682743874:AAFe-9mXdjoM0l9_77SYAmn5AG0Kqo7pp4k", use_context= True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text="Get a random hadiths")

dispatcher.add_handler(CommandHandler("start", start))

def get_hadith():

    # get api request link from sunnah.com
    url = "https://api.sunnah.com/v1/hadiths/random"

    # declaring data dictionary and required header key
    payload = "{}"
    headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}

    # getting a random hadiths from the api call
    hadith_response = requests.request("GET", url, data=payload, headers=headers)

    # converting the response data into json format acting as a dictionary
    json_hadith_response = hadith_response.json()

    # cleaning the data
    hadith_collection = json_hadith_response['collection']
    hadith_book_number = json_hadith_response['bookNumber']
    hadith_topic = json_hadith_response['hadith'][0]['chapterTitle']
    hadith_body = json_hadith_response['hadith'][0]['body']
    hadith_body_edited = hadith_body.replace("<br/>","").strip("<p></p>").replace("<b>","").replace("</b>","")
    
    random_hadith = f"From Collection of {hadith_collection.title()}\n Book of {hadith_book_number} \
        \nUnder the topic:{hadith_topic}\n HADITH:{hadith_body_edited}"
    return random_hadith

def result(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=get_hadith())

dispatcher.add_handler(CommandHandler("randomhadith", result))

def collections(update, context):
    collections_info = "You can get information about the top five collections of hadith is the islamic tradition.\n \
        They are listed below.\n 1. Bukhari."
    context.bot.send_message(chat_id = update.effective_chat.id, text = collections_info)

dispatcher.add_handler(CommandHandler("collections", collections))

updater.start_polling()
updater.idle()

