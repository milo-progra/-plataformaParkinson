import os 
from datetime import datetime

#obtener fecha actual
fecha = datetime.today().strftime('%Y_%m_%d_%H_%M')

#nombre del archivo de respaldo
respaldo = "respaldo_"+str(fecha)+".sql"

#ubicacion del mysqldumb
pathBase = "C:\archivos de programa\MySQL\MySQL Server 8.0\bin\mysqldump.exe"


try:
    os.popen(pathBase + "-u miloVan -h miloVan.mysql.pythonanywhere-services.com --set-gtid-purged=OFF --no-tablespaces --column-statistics=0 'miloVan$default'  > " + respaldo)
    print("base de datos respaldada correctamente" + respaldo)

except:
    print("ocurrio un problema no se pudo respaldar la base de datos")
    exit

  
