from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from helloapp.views import hello, AccountCreateView

app_name = 'helloapp'

urlpatterns = [
    path('helloman/', hello, name = 'hello_man'),

    path('login/', LoginView.as_view(template_name='helloapp/login.html'),
         name='login'),

    path('logout/', LogoutView.as_view(template_name='helloapp/logout.html'),
         name='logout'),

    path('create/', AccountCreateView.as_view(), name = 'create')
]
