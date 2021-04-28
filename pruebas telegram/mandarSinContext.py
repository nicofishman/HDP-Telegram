import telegram

bot = telegram.Bot(token="1773821035:AAEfhwVjFLAkwx4J62hiWueVTeqoVBe-VOc")

def mandarmeMsg(chat_id,text):
    bot.send_message(chat_id,text)
    
    
id_colton= "805954751"
for i in range(100):
    mandarmeMsg(id_colton,"la concha de tu madre")