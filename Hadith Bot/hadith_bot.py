import requests
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

updater = Updater(token="1682743874:AAFe-9mXdjoM0l9_77SYAmn5AG0Kqo7pp4k")
dispatcher = updater.dispatcher

def choices(bot, update):
    options = [
            [InlineKeyboardButton("Get a random Hadith", callback_data="randomhadiths"),

            ]
    ]

    reply = InlineKeyboardMarkup(options)
    bot.send_message(chat_id=update.message.chat_id, text = "Choose an option", reply_markup = reply)

dispatcher.add_handler(CommandHandler("hadiths", choices))

def get_hadith(bot, update):

    data = update.callback_query.data
    hadith = ""

    if (data == "randomhadiths"):

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

    bot.edit_message_text(chat_id = update.callback_query.message.chat_id,
            text = hadith,
            message_id = update.callback_query.message.message_id)

dispatcher.add_handler(CallbackQueryHandler(get_hadith))


updater.start_polling()
updater.idle()

#print(f"From Collection of {hadith_collection.title()}")
#print(f"Book of {hadith_book_number}")
#print(f"Under the topic:{hadith_topic}")
#print(f"Hadith:{hadith_body_edited}")