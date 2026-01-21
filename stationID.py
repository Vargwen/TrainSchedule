import requests
import os
import json
from dotenv import load_dotenv

# We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

def stationByName(gare):
    # The API endpoint and call
    url = "https://api.sncf.com/v1/coverage/sncf/places"
    response = requests.get(url, auth=(TOKEN, ""), params={"q": gare})
    data = response.json()

    # We create a new list to store the stations found and not the places
    stations = []

    # We filter the response and store stations in our new list
    for place in data.get("places", []):
        if place.get("embedded_type") == "stop_area":
            stations.append(place)
    
    # We print the stations found
    if len(stations) > 1:
        for i, gare in enumerate(stations):
            print(f"{i + 1} - {gare['name']}")

    #If there is only one station, we return its ID
    if len(stations) == 1:
        gare_choisie = stations[0]
        print(f"Gare trouvée : {gare_choisie['name']} (ID: {gare_choisie['id']})")
        return gare_choisie["id"]
    
    #If there is more than one station, we ask the user to choose, and we return its ID
    if len(stations) > 1:
        while True:
            choix = input(f"Quelle gare souhaitez-vous choisir ? (1 à {len(stations)}) : ")
            try:
                # We try to convert the input to an integer
                index = int(choix) - 1
                
                # We check the number is valid
                if 0 <= index < len(stations):
                    gare_choisie = stations[index]
                    print(f"Vous avez choisi : {gare_choisie['name']} (ID: {gare_choisie['id']})")
                    return gare_choisie["id"]
                    break  # Leave the loop if it's all good
                else:
                    print(f"Veuillez choisir un nombre entre 1 et {len(stations)}.")
                    
            except ValueError:
                # If int conversion fails
                print("Erreur : Ce n'est pas un nombre. Veuillez recommencer.")