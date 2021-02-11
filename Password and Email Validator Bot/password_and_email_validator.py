import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '1654757071:AAHoiYZJkX1Ejt1DYznFLKC0M-CfGUOE0Mk'
updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher


def email_validator(email):
    email_regex = re.compile(r'''(

    [a-zA-Z0-9._%+-]+           #username
    @                           #@ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})           #dot-something

    )''', re.VERBOSE)

    if email_regex.search(email):
        return f"{email} is a valid email"
    else:
        return f"{email} is not a valid email"

#email_validator("musaww@hhhe")

def validator(update: Update, context: CallbackContext):
    update.message.reply_text(email_validator(update.message.text))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, validator))


updater.start_polling()
updater.idle()

