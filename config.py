from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25713846")
    API_HASH = environ.get("API_HASH", "ca57c019f37ab7bf0bd9caead4846c88")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6935611107:AAFTtCKhhJgaa_jXo7er17KK9TmRzPTau_8") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ab123456789ab321:oph3WwTQWbG1FY0h@cluster0.w4ql1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5768102179').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
