from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):

    if request.method == 'POST':
        url = 'http://api.cne.cl/v3/combustibles/vehicular/estaciones'
        token = '6EJnyHG4YE'
        params = {'token': token}

        if request.POST['sel-region'] != '0':
            params['region'] = request.POST['sel-region']
        response = requests.get(url, params)

        if response.status_code == 200:
            data = response.json()
            bencina_list = data['data']
            return render(request, 'bencina/bencina.html', {'bencina_list': bencina_list})

    return render(request, 'bencina/bencina.html')
