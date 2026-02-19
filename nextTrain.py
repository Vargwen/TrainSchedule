import requests
import os
import json
from dotenv import load_dotenv
from dateformat import dateformat
import datetime

# We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN_SNCF")

#Get the next train from the station ID
def nextTrainFromStationID(station_id, time):
    # Call to the SNCF API
    url = f"https://api.sncf.com/v1/coverage/sncf/stop_areas/{station_id}/departures"
    response = requests.get(url, auth=(TOKEN, ""), params={"datetime": time, "count": 5})
    data = response.json()

    # Create a list to store informations
    informations = []

    for departure in data.get("departures", []):
        stop_time = departure.get("stop_date_time", {})
        
        # 1. Récupération des deux heures (Format SNCF: YYYYMMDDTHHMMSS)
        raw_planned = stop_time.get("base_departure_date_time")
        raw_real = stop_time.get("departure_date_time")
        
        # 2. Conversion en objets datetime pour le calcul
        fmt = "%Y%m%dT%H%M%S"
        planned_dt = datetime.strptime(raw_planned, fmt)
        real_dt = datetime.strptime(raw_real, fmt)
        
        # 3. Calcul du retard
        delay_delta = real_dt - planned_dt
        delay_minutes = int(delay_delta.total_seconds() / 60)
        
        # 4. Formatage du message
        destination = departure.get("display_informations", {}).get("direction")
        train_number = departure.get("display_informations", {}).get("headsign")
        
        status = "✅ À l'heure"
        if delay_minutes > 0:
            status = f"⚠️ Retard de {delay_minutes} min"
        elif delay_minutes < 0:
            status = f"🚀 En avance de {-delay_minutes} min"

        msg = (f"Train {train_number} vers {destination}\n"
               f"   Prévu: {planned_dt.strftime('%H:%M')} | "
               f"Réel: {real_dt.strftime('%H:%M')} -> {status}")
        
        informations.append(msg)

    return informations