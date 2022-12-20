#from dbhelper import DBHelper
from datetime import date #Importar fecha
import datetime
from django.utils.crypto import get_random_string
from config import *
from dbhelper import *
import telebot  #pip install pyTelegramBotAPI
from telebot.types import ForceReply #citar un mensaje
from telebot.types import ReplyKeyboardMarkup #Para crear botones


#Inicimos conexion a la base de datos
db = DBHelper()
#instanciamos el bot de telegram
bot = telebot.TeleBot(telegram_token)

#comandos de ayuda
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def cmd_start(message):
    bot.send_message(message.chat.id, "-Usa el comando /animo para introducir su estado de animo \n\n -Usa el comando /automonitoreo para introducir su estado de Automonitoreo \n\n -Usa el comando /mi_id para saber su id de telegram")


#comando para obtener id de telegram
@bot.message_handler(commands=['mi_id'])
def cmd_idTelegram(message):
    bot.send_message(message.chat.id, f"Tu id de telegram es: \n {str(message.chat.id)} ")


#se obtiene una respuesta de animo del usuario
@bot.message_handler(commands=['animo'])
def cmd_animo(message):
    
    user = db.select_user(message.chat.id)
    if user == ():
        bot.send_message(message.chat.id, f"Tu ID Telegram: {message.chat.id}, no se encuentra asociado con ningun usuario")
    else:
        #definir 2 botones
            #one_time_keyboard = define si los botones desaparecen una vez respondida la pregunta
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True, 
            input_field_placeholder="Pulsa un boton",
            resize_keyboard=True
            )
            
        list = db.select_animo()

        for i in list:
            print(i[0])
            markup.add(i[0])

        #guardar la respuesta del usuario en msg
        msg = bot.send_message(message.chat.id, "Como te sientes el dia de hoy??  ", reply_markup=markup)
        #definimos que msg se lo entragaremos la funcion preguntar_edad
        bot.register_next_step_handler(msg, guardar_datos_usuario)


#se obtiene una respuesta de automonitoreo del usuario
@bot.message_handler(commands=['automonitoreo'])
def cmd_automonitoreo(message):
    
    user = db.select_user(message.chat.id)
    if user == ():
        bot.send_message(message.chat.id, f"Tu ID Telegram: {message.chat.id}, no se encuentra asociado con ningun usuario")
    else:
        #definir 2 botones
            #one_time_keyboard = define si los botones desaparecen una vez respondida la pregunta
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True, 
            input_field_placeholder="Pulsa un boton",
            resize_keyboard=True
            )
            
        list = db.select_estado_automonitoreo()

        for i in list:
            print(i[0])
            markup.add(i[0])

        #guardar la respuesta del usuario en msg
        msg = bot.send_message(message.chat.id, "Como te sientes el dia de hoy??  ", reply_markup=markup)
        #definimos que msg se lo entragaremos la funcion preguntar_edad
        bot.register_next_step_handler(msg, guardar_datos_automonitoreo)


#se inicia el proceso de grabacion del audio
@bot.message_handler(commands=['audio'])
def cmd_audio(message):
    
    user = db.select_user(message.chat.id)
    if user == ():
        bot.send_message(message.chat.id, f"Tu ID Telegram: {message.chat.id}, no se encuentra asociado con ningun usuario")
    else:
        msg = bot.send_message(message.chat.id, "Ahora grabe su mensaje de voz.")
        print(f"Grabando un audio del usuario: {message.chat.id} ")

        bot.register_next_step_handler(msg, voice_processing)


#se guarda el audio enviado por el usuario
@bot.message_handler(content_types=['voice'])
def voice_processing(message):

    token = get_random_string(length=6)
    file_info = bot.get_file(message.voice.file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    with open(f'media/audios/{token}new_file2.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)


    username = db.select_username(message.chat.id)
    user= "".join(map(str,username))
    fecha = datetime.datetime.now()+ datetime.timedelta(seconds=10800)

    db.insert_audio(fecha,new_file.name,int(user[1]))
    # print(new_file.name)
    db.update_audio(str(new_file.name))
    bot.send_message(message.chat.id, "Su mensaje de voz se a guardado Correctamente. \n\nGracias.")
    print()

    print(f"Se a guardado correctamente un audio del usuario {message.chat.id}")
    

#se llama a la query para guardar los datos en la tabla automonitoreos
def guardar_datos_automonitoreo(message):
    username = db.select_username(message.chat.id)
    id_automonitoreo = db.select_id_automonitoreo(message.text)
    user= "".join(map(str,username))
    automonitoreo= "".join(map(str,id_automonitoreo))
    fecha = datetime.datetime.now()+ datetime.timedelta(seconds=10800)
    db.insert_automonitoreo(fecha,int(automonitoreo[1]),int(user[1]))
    bot.send_message(message.chat.id, f"Su automonitoreo se a guardado como: \n\n {message.text}")
    print()
    print("Datos Guardados")
    print()


#se llama a la query para guardar los datos en estados de animos
def guardar_datos_usuario(message):
    username = db.select_username(message.chat.id)
    id_animo = db.select_id_animo(message.text)
    user= "".join(map(str,username))
    animo= "".join(map(str,id_animo))
    fecha = datetime.datetime.now() + datetime.timedelta(seconds=10800)
    db.insert_animo(fecha,int(animo[1]),int(user[1]))
    bot.send_message(message.chat.id, f"Su estado de animo se a guardado como: \n\n {message.text}")
    print(fecha)
    print("Datos Guardados")
    print()

       
if __name__ == '__main__':
    print("iniciando el bot")
    # bucle infinito que comprueba si hay nuevos mensajes
    bot.infinity_polling()
















