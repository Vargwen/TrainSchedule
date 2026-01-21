import requests
import os
import json
from dotenv import load_dotenv
from stationID import stationByName
from nextTrain import nextTrainFromStationID
from datetime import datetime

#We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

#We ask user where does he want to go
nom_gare = input("Which station to you want to check? ")

#We get the station ID
gare = stationByName(nom_gare)

#We get the next trains from this station
current_time = datetime.now().strftime("%Y%m%dT%H%M%S")
nextTrainFromStationID(gare, current_time)