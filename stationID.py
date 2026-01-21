import requests
import os
import json
from dotenv import load_dotenv

#We load the token from the .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

#We ask user where does he want to go
nom_gare = input("De quelle ville partez-vous?")


def stationByName(gare):
    print("Gare demandée: " + gare)

    #The API endpoint
    url = "https://api.sncf.com/v1/coverage/sncf/places"

    response = requests.get(url, auth=(TOKEN, ""), params={"q": gare})
    data = response.json()

    #Print all the stations found with a stop_area ID
    compteur_gares = 0
    if "places" in data:
        for place in data["places"]:
            if place["id"].startswith("stop_area:"):
                compteur_gares += 1
                print(str(compteur_gares) + " - "+place["name"])

        if compteur_gares == 1:
            gare_choisie = data["places"][0]
            print(f"Gare unique trouvée : {gare_choisie['name']} (ID: {gare_choisie['id']})")
            return gare_choisie
        #If there is more than one station, we ask the user to choose
        if compteur_gares > 1:
            while True:
                choix = input(f"Quelle gare souhaitez-vous choisir ? (1 à {compteur_gares}) : ")
                
                try:
                    # We try to convert the input to an integer
                    index = int(choix) - 1
                    
                    # We check the number is valid
                    if 0 <= index < len(data["places"]):
                        gare_choisie = data["places"][index]
                        print(f"Vous avez choisi : {gare_choisie['name']} (ID: {gare_choisie['id']})")
                        return gare_choisie
                        break  # Leave the loop if it's all good
                    else:
                        print(f"Veuillez choisir un nombre entre 1 et {compteur_gares}.")
                        
                except ValueError:
                    # If int conversion fails
                    print("Erreur : Ce n'est pas un nombre. Veuillez recommencer.")
    else:
        print("Aucune gare trouvée avec ce nom.")
        
stationByName(nom_gare)