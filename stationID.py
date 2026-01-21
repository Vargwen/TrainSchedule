import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

nom_gare = input("De quelle ville partez-vous?")


def stationByName(gare):
    print("Gare demandée: " + gare)

    #The API endpoint
    url = "https://api.sncf.com/v1/coverage/sncf/places"

    response = requests.get(url, auth=(TOKEN, ""), params={"q": gare})
    print(response.json())

stationByName(nom_gare)