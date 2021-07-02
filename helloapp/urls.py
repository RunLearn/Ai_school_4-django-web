from django.urls import path

from helloapp.views import hello

app_name = 'helloapp'

urlpatterns = [
    path('hello man/', hello, name = 'hello_man')
]