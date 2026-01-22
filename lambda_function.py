import os
import requests
from datetime import datetime

# Import the functions
from stationID import stationByName
from nextTrain import nextTrainFromStationID
from callBot import sendMessage

def lambda_handler(event, context):
    try:
        gare = "stop_area:SNCF:87682443"

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

        return {
                'statusCode': 200,
                'body': json.dumps(f"Notification envoyée pour {nom_gare}")
            }

    except Exception as e:
        print(f"Erreur : {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Erreur lors de l'exécution : {str(e)}")
        }

