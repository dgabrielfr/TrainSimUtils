import requests

def get_map_data():
    data = {}
    pos_url = 'http://localhost:31270/get/DriverAid.PlayerInfo'
    speed_url = 'http://localhost:31270/get/CurrentDrivableActor.Function.HUD_GetSpeed'

    payload = {}
    headers = {
        'DTGCommKey': '5c8N1tnWPtApKPkUzCufVp5XmsbQKcEEiDgt3wUgiHk='
    }

    # Coordinates
    response_position = requests.request("GET", pos_url, headers=headers, data=payload)
    response_position_json = response_position.json()

    if response_position_json["Result"] == "Success":
        location = response_position_json["Values"]["geoLocation"]
        data['lat'] = location['latitude']
        data['lng'] = location['longitude']

    else:
       print("Erreur lors de la récupération de la position du train")
        # messages.warning(request, 'Erreur lors de la récupération de la position du train')

    # Speed
    response_speed = requests.request("GET", speed_url, headers=headers, data=payload)
    response_speed_json = response_speed.json()

    if response_speed_json["Result"] == "Success":
        data['speed_ms'] = response_speed_json["Values"]["Speed (ms)"]

    else:
        print("Erreur lors de la récupération de la vitesse du train")

    return data
