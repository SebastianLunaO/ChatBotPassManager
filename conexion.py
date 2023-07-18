import telepot
TOKEN ='BotToken'
TelegramBot=telepot.Bot(TOKEN)
user_id=0

def Enviar(mensaje):
    TelegramBot.sendMessage(user_id,mensaje)
    return 1