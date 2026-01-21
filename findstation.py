import requests

def test_api():
    # 1. Votre Token (Vérifiez qu'il n'y a pas d'espace avant ou après)
    token = "76952d41-f4a1-4919-9233-241e87faec8a"
    
    # 2. Utilisons un ID standard (Gare de Lyon à Paris pour le test)
    # Si ça marche, on remettra Lyon Part Dieu
    gare_id = "stop_area:SNCF:87686006" 
    
    # Construction de l'URL ultra-propre
    url = f"https://api.sncf.com/v1/coverage/sncf/stop_areas/{gare_id}/departures"
    
    try:
        # On fait la requête
        response = requests.get(url, auth=(token, ""))
        
        print(f"Statut Code : {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if 'departures' in data and len(data['departures']) > 0:
                prochain = data['departures'][0]
                direction = prochain['display_informations']['direction']
                heure = prochain['stop_date_time']['departure_date_time']
                print(f"Connexion réussie ! Prochain train pour : {direction} à {heure}")
            else:
                print("Aucun départ trouvé pour cette gare actuellement.")
        elif response.status_code == 401:
            print("Erreur : Votre Token est invalide (401).")
        elif response.status_code == 404:
            print("Erreur : L'ID de la gare est introuvable (404).")
        else:
            print(f"Erreur imprévue : {data}")
            
    except Exception as e:
        print(f"Erreur de script : {e}")

test_api()