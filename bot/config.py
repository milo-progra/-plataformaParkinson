#bibloteca pip install python-decouple que te permite utilizar variables de entorno
from decouple import config

telegram_token = config('TELEGRAM_TOKEN')