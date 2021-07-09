from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    if request.method == "POST":
        return render(request, 'helloapp/helloworld.html',
                      context={'text': 'POST METHOD!'})
    else:
        return render(request, 'helloapp/helloworld.html',
                      context={'text': 'GET METHOD!'})
