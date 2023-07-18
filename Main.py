import conexion
import telepot
import time
from conexion import Enviar
import json
import os
import sys
from pprint import pprint
from telepot.loop import MessageLoop
from conexion import TelegramBot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from PassManage import taking
from secrets import compare_digest
started=0
#jsonData=json.loads(Inicio())
def opciones(entrada):
    print(entrada)
    respuesta=taking(entrada)
    return respuesta
    
def on_chat_message(msg):
    Cuentas=['Gmail','Paypal','Outlook']
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    i=0
    while compare_digest(msg['text'],"contramain"):
        if i==3:
            break
        keyboard=InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Obtener', callback_data=str(i+1))],
               ])
        TelegramBot.sendMessage(chat_id, Cuentas[i], reply_markup=keyboard)
        i=i+1

    
    
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    aws=opciones(int(query_data))

    TelegramBot.answerCallbackQuery(query_id, text='Constraseña:')
    Enviar(aws)
    

#pprint(Inicio())
MessageLoop(TelegramBot,{'chat':on_chat_message,'callback_query':on_callback_query}).run_as_thread()
#payload=json.loads(raw)
while 1: 
    time.sleep(10)
