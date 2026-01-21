import requests
import os
import json
from dotenv import load_dotenv
from stationID import stationByName

#We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

#We ask user where does he want to go
nom_gare = input("Vers quelle ville voulez-vous aller? ")

#We get the station ID
gare = stationByName(nom_gare)