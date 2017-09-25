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

    with open('static/images/background/info.json', 'r') as json_file:
        images_info = json.load(json_file)

    shuffle(images_info)

    return render(request, 'index.html', {
        'images_info_str': json.dumps(images_info),
        'images_info': images_info,
        })
