import requests
from django.http import JsonResponse

from TrainSimUtils.settings import TSW_HTTP_KEY


def get_map_data():
    data = {}
    pos_url = 'http://localhost:31270/get/DriverAid.PlayerInfo'
    speed_url = 'http://localhost:31270/get/CurrentDrivableActor.Function.HUD_GetSpeed'

    payload = {}
    headers = {
        # from C:\Users\[YOUR USERNAME]\Documents\My Games\TrainSimWorld5\Saved\Config
        # now in settings
        'DTGCommKey': TSW_HTTP_KEY
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
        data['speed_kmh'] = response_speed_json["Values"]["Speed (ms)"] * 3.6

    else:
        print("Erreur lors de la récupération de la vitesse du train")
        data['speed_ms'] = 0
        data['speed_kmh'] = 0

    return data


def get_data_json(request):
    """
    Endpoint JSON pour le polling côté front.
    Renvoie: {"lat": float, "lng": float, "speed_kmh": float}
    """
    data = get_map_data()
    return JsonResponse({
        'lat': data.get('lat'),
        'lng': data.get('lng'),
        'speed_kmh': data.get('speed_kmh'),
    })

