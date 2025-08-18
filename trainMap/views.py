from django.http import HttpResponse
from django.shortcuts import render

from trainMap.models import TrainData
from trainMap.utils import get_map_data


def test(request):
    return HttpResponse("Bonjour, la route 'test' fonctionne !")

def get_data(request):
    data = get_map_data()
    return render(request, 'map.html', {'lat': data['lat'], 'lng': data['lng'], 'speed_ms': data['speed_ms']})
