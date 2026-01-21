import requests
import os
import json
from dotenv import load_dotenv
from dateformat import dateformat

# We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

#Get the next train from the station ID
def nextTrainFromStationID(station_id, time):
    url = f"https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:SNCF:87682443/departures"
    response = requests.get(url, auth=(TOKEN, ""), params={"datetime": time, "count": 5})
    data = response.json()
    for departure in data.get("departures", []):
        destination = departure.get("display_informations", {}).get("direction")
        train_number = departure.get("display_informations", {}).get("headsign")
        departure_time = dateformat(departure.get("stop_date_time", {}).get("departure_date_time"))
        print(f"Train {train_number} to {destination} departs at {departure_time}")