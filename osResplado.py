import os
from datetime import datetime

now = datetime.now()
fecha = str(now.date())

cmd_command = f"mysqldump -u miloVan -h miloVan.mysql.pythonanywhere-services.com --set-gtid-purged=OFF --no-tablespaces --column-statistics=0 'miloVan$default'  > {fecha}.sql"
os.system(cmd_command)



