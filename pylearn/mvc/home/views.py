from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum

import json

from models import Money
from models import Player

def show_db(request):

    html = ''
    for i in range(1, 6):
        m = Money.objects.get(id=i)
        html += "<h1>id = {} amount ={}<h1>".format(i, m.amount) + '\n'
    return HttpResponse(html)

def show_db_id(request, id):

    m = Money.objects.get(id=id)
    html = '''<h1>{}<h1>'''.format(m.amount)
    return HttpResponse(html)

def p_info(request, player_id):
    return HttpResponse("Hello, user with id: {}".format(player_id))

def p_list(request):
    print("DEBUG: request.GET is {}".format(request.GET))
    return HttpResponse("Hello, great players: {}".format(request.GET["ids"]))

def test2(request):
    template_data = {
        "player_list": Player.objects.all(),
        "version": "1.0"
    }
    return render(request, 'test2.html', template_data)


def hw1(request):
    '''
    from django.core import serializers
    '''
    data = serializers.serialize('json', Money.objects.all(), fields=('currency_id', 'amount'))
    return HttpResponse(data)

def hw3(request):
    return HttpResponse(json.dumps(Player.objects.all().values('id', 'email')),
             content_type='application/json; charset=UTF-8', status=200)


def hw2(request, id):
    money_by_id_rows = Money.objects.filter(player_id=id)
    return HttpResponse(money_by_id_rows)
