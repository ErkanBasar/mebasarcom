from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response

from django.conf import settings


def handler404(request):
	response = render_to_response('404.html', {},context_instance=RequestContext(request))
	response.status_code = 404
	return response

def handler500(request):
	response = render_to_response('500.html', {},context_instance=RequestContext(request))
	response.status_code = 500
	return response


def serveKeybase(request):
	return render(request, 'keybase.txt', {})


class Home(View):

	def get(self, request):


		return render(request, 'index.html', {
		})
