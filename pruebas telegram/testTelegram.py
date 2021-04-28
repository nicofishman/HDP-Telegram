import telebot
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import MessageEntity
import responses as R


keys="1773821035:AAEfhwVjFLAkwx4J62hiWueVTeqoVBe-VOc"
bot = telebot.TeleBot("")

def start_command(update,context):
    update.message.reply_text("Escribime algo papá")
    
def help_command(update,context):
    update.message.reply_text("Dios te va a ayudar la concha tuya")

def miMensaje(update,context,user_id,texto):
    update.message.send(user_id,texto)

def handle_message(update,context):
    text=str(update.message.text).lower()
    response = R.sample_responses(text)
    
    update.message.reply_text(response)
    
def error(update,context):
    print(f"Update {update} caused error {context.error}")
    
    
    
def main():
    updater = Updater(keys,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("ayuda",help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()
    
main()