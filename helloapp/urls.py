from django.urls import path

from helloapp.views import hello, AccountCreateView

app_name = 'helloapp'

urlpatterns = [
    path('helloman/', hello, name = 'hello_man')

    path('create/',AccountCreateView.as_view(), name = 'create')
]
