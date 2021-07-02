from django.urls import path

from helloapp.views import hello

app_name = 'helloapp'

urlpatterns = [
    path('helloman/', hello, name = 'hello_man')
]