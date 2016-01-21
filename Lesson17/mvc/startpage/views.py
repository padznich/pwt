from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def say_hello(request):

    html = '''<h1>Hello!<h1>'''

    return HttpResponse(html)