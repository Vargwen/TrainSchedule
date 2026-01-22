import requests
import os
import json
from dotenv import load_dotenv
from datetime import datetime

# Import the functions
from stationID import stationByName
from nextTrain import nextTrainFromStationID
from callBot import sendMessage

#We ask user where does he want to go
nom_gare = input("Which station to you want to check? ")

#We get the station ID
gare = stationByName(nom_gare)

#We get the next trains from this station
current_time = datetime.now().strftime("%Y%m%dT%H%M%S")
response = nextTrainFromStationID(gare, current_time)

# We retrieve today's date
date_aujourdhui = datetime.now().strftime("%d/%m/%Y")

# Make sure the list is not empty
if not response:
    message_final = "⚠️ Aucun départ prévu ce matin dans cette gare."
else:
    message_final = f"🚉 PROCHAINS DÉPARTS ({date_aujourdhui}) :\n\n" + "\n".join(response)

# Process the data then send the data to the Telegram bot
sendMessage(message_final)