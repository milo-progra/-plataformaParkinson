import MySQLdb # pip install mysqlclient
#bibloteca pip install python-decouple que te permite utilizar variables de entorno
from decouple import config


class DBHelper:
    def __init__(self):

        self.mydb = MySQLdb.connect(

            host        =   config('HOST'), 
            user        =   config('USER'), 
            password    =   config('PASSWORD'),
            database    =   config('NAME'),

            # host        =   'vozparkinson.mysql.pythonanywhere-services.com', 
            # user        =   'vozparkinson', 
            # password    =   "MYSQL12345",
            # database    =   "vozparkinson$default",
            

            )

#se llama al usuario compatible con su id_telegram
    def select_user(self, id_telegram):
            cursor = self.mydb.cursor()
            query = f"SELECT * FROM {config('NAME')}.paciente_paciente where telegram_paciente  = %s"
            # query = "SELECT * FROM vozparkinson$default.app_paciente where telegram_paciente  = %s"
            adr = (id_telegram, )
            cursor.execute(query,adr)
            myresult = cursor.fetchall()
            return myresult

#se llaman todos los estados de animos
    def select_animo(self):
            cursor = self.mydb.cursor()
            query = f"SELECT nombre_animo FROM {config('NAME')}.paciente_animo"
            # query = "SELECT nombre_animo FROM vozparkinson$default.app_animo"
            cursor.execute(query)
            myresult = cursor.fetchall()
            return myresult

#se llaman todos los estados de automonitoreo
    def select_estado_automonitoreo(self):
            cursor = self.mydb.cursor()
            query = f"SELECT estado_monitoreo  FROM {config('NAME')}.app_estado_monitoreo"
            # query = "SELECT estado_monitoreo  FROM vozparkinson$default.app_estado_monitoreo"

            cursor.execute(query)
            myresult = cursor.fetchall()
            return myresult

#se busca la id del estado monitoreo seleccionado
    def select_id_automonitoreo(self, estado_monitoreo):
            cursor = self.mydb.cursor()
            query = f"SELECT id_estado_monitoreo FROM {config('NAME')}.app_estado_monitoreo where estado_monitoreo  = %s" 
            # query = "SELECT id_estado_monitoreo FROM vozparkinson$default.app_estado_monitoreo where estado_monitoreo  = %s"
            adr = (estado_monitoreo, )
            cursor.execute(query,adr)
            myresult = cursor.fetchall()
            return myresult


#se busca el id del estado de animo seleccionado 
    def select_id_animo(self, nombre_animo):
            cursor = self.mydb.cursor()
            query = f"SELECT id_animo FROM {config('NAME')}.paciente_animo where nombre_animo  = %s"
            # query = "SELECT id_animo FROM vozparkinson$default.app_animo where nombre_animo  = %s"
            adr = (nombre_animo, )
            cursor.execute(query,adr)
            myresult = cursor.fetchall()
            return myresult

#se busca el username del usuario con el id_telegram compatible
    def select_username(self, id_telegram):
            cursor = self.mydb.cursor()
            query = f"SELECT username_paciente_id FROM {config('NAME')}.paciente_paciente where telegram_paciente  = %s"
            # query = "SELECT username_paciente_id FROM vozparkinson$default.app_paciente where telegram_paciente  = %s"
            adr = (id_telegram, )
            cursor.execute(query,adr)
            myresult = cursor.fetchall()
            return myresult



            
#se insertan los datos a la tabla Estado_animo
    def insert_animo(self, fecha_estado_animo, animo_id,username_paciente_id):
        cursor = self.mydb.cursor()
        query = f"INSERT INTO {config('NAME')}.app_estado_animo (fecha_estado_animo, animo_id, username_paciente_id) VALUES (%s, %s, %s)"
        # query = "INSERT INTO vozparkinson$default.app_estado_animo (fecha_estado_animo, animo_id, username_paciente_id) VALUES (%s, %s, %s)"
        valores = (fecha_estado_animo, animo_id,username_paciente_id)
        cursor.execute(query, valores)
        self.mydb.commit()


#se insertan los datos a la tabla Automonitoreo
    def insert_automonitoreo(self, fecha_automonitoreo, estado_monitoreo_id, username_paciente_id):
        cursor = self.mydb.cursor()
        query = f"INSERT INTO {config('NAME')}.app_automonitoreo (fecha_automonitoreo, estado_monitoreo_id, username_paciente_id) VALUES (%s, %s, %s)"
        # query = "INSERT INTO vozparkinson$default.app_automonitoreo (fecha_automonitoreo, estado_monitoreo_id, username_paciente_id) VALUES (%s, %s, %s)"
        valores = (fecha_automonitoreo, estado_monitoreo_id, username_paciente_id)
        cursor.execute(query, valores)
        self.mydb.commit()
    
#se insertan los audios enviados en la tabla Audios
    def insert_audio(self, timestamp, url_archivo_audio, username_paciente_id):
        cursor = self.mydb.cursor()
        query = f"INSERT INTO {config('NAME')}.app_audio (timestamp, url_archivo_audio, username_paciente_id) VALUES (%s, %s, %s)"
        # query = "INSERT INTO vozparkinson$default.app_audio (timestamp, url_archivo_audio, username_paciente_id) VALUES (%s, %s, %s)"
        valores = (timestamp, url_archivo_audio, username_paciente_id)
        cursor.execute(query, valores)
        self.mydb.commit()

#se actualiza y cambia el nombre de la url guardada
    def update_audio(self,url_archivo_audio ):
        cursor = self.mydb.cursor()
        query = f"UPDATE {config('NAME')}.app_audio SET url_archivo_audio = SUBSTRING(%s, 7) WHERE url_archivo_audio = %s"
        # query = "UPDATE vozparkinson$default.app_audio SET url_archivo_audio = SUBSTRING(%s, 45) WHERE url_archivo_audio = %s"
        valores = (url_archivo_audio,url_archivo_audio)
        cursor.execute(query, valores)
        self.mydb.commit()