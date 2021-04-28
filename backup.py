import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pandas as pd
from pprint import pprint

keys=""
bot = telegram.Bot(token=keys)
filedata = pd.read_excel(r"D:\DOCUments D\GoeTemp\hdp meu\hdp.xlsx")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#TODO: CAMBIAR LINEA 13 A DICCIONARIO + LINEA 24 FIX 
rooms=[]
def createRoom(update,context):
    if (len(context.args))!= 2:
        context.bot.send_message(chat_id=update.effective_chat.id,text=f"<i>Syntaxis error.</i>\n<b>/create <i>RoomName Nickname</i></b>", parse_mode=telegram.ParseMode.HTML)
        return 0
    cartasBlancas = filedata["CartasBlancas"].values.tolist()
    cartasNegrasExcel = filedata["CartasNegras"].values.tolist()
    cartasNegras = [x for x in cartasNegrasExcel if str(x) != 'nan']
    players={}
    newRoom=[context.args[0],cartasBlancas,cartasNegras, update.effective_chat.id, 0, players]
    players[context.args[1]] = update.effective_chat.id
    rooms.append(newRoom)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Successfuly created " + context.args[0])
    pprint(rooms)

def joinRoom(update,context):
    #TODO: filtro para que no haya 2 players con el mismo nick
    for room in rooms:
        if room[0] == context.args[0]:
            room[-1][context.args[1]] = update.effective_chat.id
            pprint(room)
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Succesfully joint to room " + str(context.args[0]))
            return 0
    context.bot.send_message(chat_id=update.effective_chat.id, text="Room not found. Create one instead")

def helpCommand(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='<b></b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML)
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.from_user.first_name)

def iniciarJuego(indexRoom):
    print("SALA " + str(rooms[indexRoom][0]) + " EMPEZÓ")
    players_id=rooms[indexRoom][-1].values()
    for player_id in players_id:
        bot.send_message(player_id, "Room " + str(rooms[indexRoom][0]) + " has started!!!") 

def startGame(update,context):
    if len(rooms) < 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="There are no rooms online. Create one with /create") 
        return 0
    for i in range(len(rooms)):
        if rooms[i][0] == context.args[0]:
            if rooms[i][-3] == update.effective_chat.id:
                iniciarJuego(i)
                return 0
            context.bot.send_message(chat_id=update.effective_chat.id, text="Only the creator of the room can start the game. Ask him/her to start it")
            return 0
        context.bot.send_message(chat_id=update.effective_chat.id, text="That room does not exist")
        return 0


def main():
    updater = Updater(keys,use_context=True)
    dp = updater.dispatcher

    help_handler = CommandHandler("help",helpCommand)
    create_handler = CommandHandler("create",createRoom)
    join_handler = CommandHandler("join",joinRoom)
    startGame_handler = CommandHandler("startGame",startGame)
    
    
    dp.add_handler(help_handler)
    dp.add_handler(create_handler)
    dp.add_handler(join_handler)
    dp.add_handler(startGame_handler)
    
    updater.start_polling()
    updater.idle()
    
main()


