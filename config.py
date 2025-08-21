from os import environ

API_ID = int(environ.get("API_ID", "27693415"))
API_HASH = environ.get("API_HASH", "8dc020d35ff99813b494f20955d8c724")
BOT_TOKEN = environ.get("BOT_TOKEN", "8455094377:AAGcAPZ0KPOrMHX3MRu5Al2NULnpOl4xcMA")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003031557207"))
ADMINS = int(environ.get("ADMINS", "8115758627"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://ledaxad522:FiJVewcu6tkNBN2q@cluster0.cealr1i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "Cluster0")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
