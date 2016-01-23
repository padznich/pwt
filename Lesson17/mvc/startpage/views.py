from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

import datetime

def test1(request):
    template_data = {
        "first_name": "Django",
        "last_name": "Unchained",
        "version": "1.0",
        "created": datetime.datetime.now()
    }
    return render(request, 'test1.html', template_data)