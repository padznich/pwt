from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from models import Money

def show_db(request):

    m = Money.objects.get(id=1)
    html = '''<h1>{}<h1>'''.format(m.value)
    #html = '''<h1>{}<h1>'''.format('--t--')

    return HttpResponse(html)