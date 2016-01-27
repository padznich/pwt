from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import PlayerChangeForm

from models import Player

def change_player(request, user_id):
    player = Player.objects.get(id=user_id)
    template_data = {
        "player": player
    }
    if request.method == "POST":
        player.email = request.POST["email"]
        player.name = request.POST["name"]
        player.save()
        return render(request, "form192.html", template_data)

    return render(request, "form191.html", template_data)


def change_player_django_form(request, player_id):
    player = Player.objects.get(id=player_id)
    form = PlayerChangeForm(data={"email": player.email, "name": player.name})
    if request.method == 'POST':
        form = PlayerChangeForm(request.POST)
        if form.is_valid():
            player.email = form.cleaned_data["email"]
            player.name = form.cleaned_data["name"]
            player.save()
            return HttpResponseRedirect("/player_changed/%d" % player.id)

    template_data = {
        "form": form,
        "player": player
    }

    return render(request, 'form193.html', template_data)

def player_changed(request, player_id):
    template_data = {
        "player_id": player_id
    }
    return render(request, "form192.html", template_data)