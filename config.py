# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25976192")

API_HASH = os.environ.get("API_HASH", "8ba23141980539b4896e5adbc4ffd2e2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7871528004:AAGvbpoZ2bM2Oor7vH8Zo9vBB-0d4oZwjL8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "CARTOONFUNNY02") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Rahat")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://rahatsarker224:GXl1i1sRfS9USFq6@rahat.zexcpsp.mongodb.net/?retryWrites=true&w=majority&appName=Rahat")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6621572366').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
