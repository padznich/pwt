from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def foo(request):
    return HttpResponse("<h1>Hello World!<h1>"
                        "<b>What are you doing here?<b>")
