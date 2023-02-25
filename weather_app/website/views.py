from django.shortcuts import render
from django.conf import settings
import requests


def home(request):
    key = settings.API_KEY
    end_url = "https://api.weatherapi.com/v1/current.json?"
    result = None
    if request.method == 'POST':
        q = request.POST['q']
        params = {
            'key': key,
            'q': q
        }
        response = requests.get(end_url, params=params)
        result = response.json()
        return render(request, 'index.html', {'result': result})
    return render(request, 'index.html', {'result': result})
