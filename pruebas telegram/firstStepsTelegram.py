#IMPORTAR LAS MIERDAS QUE NECESITEMOS
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


#PROBLEMA: EJECUTAR FUNCIONES QUE RECIVEN UPDATE Y CONTEXT DESDE FUNCIONES DE PYTHON COMUN Y CORRIENTES.


''' 
NOTAS:
context es todo lo que tiene que ver con el bot. Se le pasa a todas las funciones para que puedan interactuar con él.
https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.callbackcontext.html están todos los valores que puede tener el context

updater.stop() frena el bot


https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples EJEMPLOS GUTHIB
'''

#Función para responderle al remitente del comando /start con un mensaje text
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    print(update.effective_chat.id)
   
#Función para mandarle a RAPO un mensaje text (comando /startRapo)
def mensajeRapo(context,texto):
    context.bot.send_message(chat_id=711287582, text="hola soy peer el bot")
    print(update.effective_chat.id)

#Función para responder a cualquier mensaje (que no sea comando) con ese mismo mensaje
def echo(update, context):
    if update.message.text in ("quien sos","quien chota sos","como te llamas"):
        context.bot.send_message(chat_id=update.effective_chat.id, text="soy Peer, el Bot")
        return 0
    print(update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="No entiendo ese comando ura")

def suma(update,context):
    inicio = 1
    inicio = int(context.args[0])
    z = int(context.args[1])
    for i in range(inicio,z+1):
        context.bot.send_message(chat_id=update.effective_chat.id, text=i)
    


updater = Updater(token="1773821035:AAEfhwVjFLAkwx4J62hiWueVTeqoVBe-VOc", use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

#Declaramos el mensaje y qué función debe activar 
start_handler = CommandHandler("start",start)
startRapo_handler = CommandHandler("startRapo",mensajeRapo)
mensaje_handler = MessageHandler(Filters.text & (~Filters.command), echo)
caps_handler = CommandHandler("caps",caps)
suma_handler = CommandHandler("suma",suma)



noCommand_handler = MessageHandler(Filters.command, unknown) #AGREGARLO ULTIMO, PORQUE SINO LOS COMANDOS QUE VENGAN DESPUES DE ESTE NO VAN A SER EJECUTADOS

#Agregamos el comando a la lista de comandos
dispatcher.add_handler(mensaje_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(startRapo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(suma_handler)



dispatcher.add_handler(noCommand_handler)


#Iniciamos el bot
updater.start_polling()