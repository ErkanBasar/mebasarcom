# import os
# import glob
import json
from random import shuffle

from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response

from django.conf import settings

def custom_404(request):
    response = render_to_response('error_page.html',
                                  {'error_code':'404',
                                   'error_message': 'The requested URL was ' \
                                                    'not found on this server.'})
    response.status_code = 404
    return response

def custom_500(request):
    response = render_to_response('error_page.html',
                                  {'error_code':'500',
                                   'error_message': 'Internal Server Error. ' \
                                                    'Please report to admins.'})
    response.status_code = 500
    return response


def serveKeybase(request):
    return render(request, 'keybase.txt', {})


def home(request):

    images_info = [
        {
            "filePath": "images/background/akyaka.jpg",
            "location": "Akyaka",
            "mapUrl": "https://goo.gl/maps/Ah2PatXKaND2"
        },
        {
            "filePath": "images/background/ayder.jpg",
            "location": "Ayder Yaylası",
            "mapUrl": "https://goo.gl/maps/73cDuwgL6At"
        },
        {
            "filePath": "images/background/fethiye-tekneler.jpg",
            "location": "Fethiye",
            "mapUrl": "https://goo.gl/maps/frPujA1mGjn"
        },
        {
            "filePath": "images/background/oludeniz.jpg",
            "location": "Ölüdeniz",
            "mapUrl": "https://goo.gl/maps/frPujA1mGjn"
        },
        {
            "filePath": "images/background/pamukkale.jpg",
            "location": "Pamukkale",
            "mapUrl": "https://goo.gl/maps/qX7Bi1YEq482"
        },
        {
            "filePath": "images/background/pokut.jpg",
            "location": "Pokut",
            "mapUrl": "https://goo.gl/maps/Gn6Eu5U1t7H2"
        }
    ]

    shuffle(images_info)

    return render(request, 'index.html', {
        'images_info_str': json.dumps(images_info),
        'images_info': images_info,
        })
