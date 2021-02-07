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



def get_collection(collection_name):
    url = f"https://api.sunnah.com/v1/collections/{collection_name}"

    payload = "{}"
    headers = {'x-api-key': 'SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk'}

    response = requests.request("GET", url, data=payload, headers=headers)

    collections = response.json()
    collections_edited = collections['collection'][0]['shortIntro']
    return collections_edited


def collections(update, context):
    collections_info = "You can get information about the top five collections of hadith is the islamic tradition.\n \
        They are listed below.\n 1. Bukhari\n 2. Muslim\n 3. Sunan Nasa-i\n 4. Sunan Abi Dawud\n 5. Jami` at-Tirmidhi\n 6. Sunan Ibn Majah"
    context.bot.send_message(chat_id = update.effective_chat.id, text = collections_info)

dispatcher.add_handler(CommandHandler("collections", collections))

def get_bukhari(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = get_collection('bukhari'))

dispatcher.add_handler(CommandHandler("bukhari",get_bukhari))

updater.start_polling()
updater.idle()

