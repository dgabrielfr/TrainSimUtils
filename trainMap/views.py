from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from trainMap.models import TrainData
from trainMap.utils import get_map_data

def test(request):
    return HttpResponse("Bonjour, la route 'test' fonctionne !")

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

def get_data(request):
    data = get_map_data()
    return render(request, 'map.html', {'lat': data['lat'], 'lng': data['lng'], 'speed_kmh': data['speed_kmh']})
