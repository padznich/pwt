

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def show_players(request):


    from start.models import players

    players_list = players.email[0]

    return HttpResponse("<h1>{}<h1>".format(players_list))