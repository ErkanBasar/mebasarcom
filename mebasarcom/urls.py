"""mebasarcom URL Configuration"""

from django.conf.urls import url
from django.contrib import admin

from main import views

handler404 = 'main.views.custom_404'

handler500 = 'main.views.custom_500'

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),

    url(r'^keybase.txt$', views.serveKeybase, name='keybase'),

    url(r'^37N38E$', views.age_puzzle, name='age_puzzle'),
]
