from django.contrib import admin

from models import Player, Money

# Register your models here.

admin.site.register([Player, Money])
#admin.site.register(Money)
