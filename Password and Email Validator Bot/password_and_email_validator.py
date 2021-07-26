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

# creating the strong password validator function
def strong_password_validator(password):
    # creating the strong password regex
    strong_password = re.compile(r'''(
        ^(?=.*[A-Z].*[A-Z])     # at least two characters
        (?=.*[!@#$&*])         # at least one of the special characters
        (?=.*[0-9].*[0-9])     # at least two numeric digits
        (?=.*[a-z].*[a-z].*[a-z]) # at least three lower case characters
        .{8,}                     # at least a total of eight characters 
        $
    )''', re.VERBOSE)
    while True:
        mo = strong_password.search(password)
        if (not mo):
            return f"Your password should have at least one special charachter, two digits.\
                    At least two uppercase and three lowercase charachter.\
                    It Should be 8+ characters in lenght.\
                    Enter another password:"
        else:
            return f"Password is strong"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("This bot validates email addresses. You Just write the email and it will tell you\
        whether it is valid or not! Select \password or \email")
def email(update: Update, context: CallbackContext):
    update.message.reply_text("Enter an email to test:")
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, email_validator))

def validator(update: Update, context: CallbackContext):
    update.message.reply_text(email_validator(update.message.text))

def pass_validator(update:Update, context: CallbackContext):
    update.message.reply_text(strong_password_validator(update.message.text))

def password(update: Update, context: CallbackContext):
    update.message.reply_text("Enter a Password to test:")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("password", password))
dispatcher.add_handler(CommandHandler("email", email))

updater.start_polling()
updater.idle()

