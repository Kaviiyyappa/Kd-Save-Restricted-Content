import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21939922"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bd2d18dd26b200480bda4cbdf2c2da30")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6757014146"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://KD-Save-Restricted-Content-Bot-v2:injEhJ90EpRSraB0@kd-save-restricted-cont.726qafr.mongodb.net/?retryWrites=true&w=majority&appName=KD-Save-Restricted-Content-Bot-v2") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "KD-Save-Restricted-Content-Bot-v2")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
