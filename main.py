from telegram.ext import *
import Responses as R
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BOT_API")
PORT = int(os.environ.get('PORT', 5000))

print("Bot started.")

def start_command(update, context):
    update.message.reply_text("Type something random to get started!")

def help_command(update, context):
    update.message.reply_text("Go get some help bruh.")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.message_handler_main_function(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error: {context.error}")

def main():
    updater = Updater(API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=API_KEY)
    updater.bot.setWebhook('https://shrouded-savannah-23341.herokuapp.com/' + API_KEY)
    updater.idle()


main()