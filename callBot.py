import requests
import os
from dotenv import load_dotenv

# We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN_TELEGRAM")
CHAT_ID = os.getenv("CHAT_ID_TELEGRAM")

def sendMessage(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.get(url, params=params)
        print(response.json())
    except Exception as e:
        print(f"Erreur de connexion : {e}")