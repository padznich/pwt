# coding=utf-8


"""
django-admin startrpoject mvc
django-admin startapp home
django-admin startapp startpage
django-admin createsuperuser pad padznich


python manage.py inspectdb > <app_name>/models.py  -- закинуть существующую DB в models.py
python manage.py makemigrations                    -- миграции
python manage.py migrate                           -- миграции

В admin.py
    from django.contrib import admin

    from models import Player           # после inspectdb в models.py появилась база откуда мы берём Player
    # Register your models here.

    admin.site.register(Player)

В models.py
            class Meta:
                    managed = False
                    verbose_name_plural = 'Money'
                    db_table = 'money'
                    db_table = 'money'


работа в python manage.py shell
https://docs.djangoproject.com/en/1.8/topics/db/queries/#limiting-querysets
>>> p = Player.objects.get(name='Monster')
>>> Player.objects.filter(created__gt='2015-12-31')[:3]
>>> Player.objects.filter(email__endswith='by')
>>> Player.objects.all().order_by('name')
>>> for w in Player.objects.all().order_by('name'):
...     print(w)
>>> from django.db.models import Sum, Avg
>>> Money.objects.filter(currency_id='BYN').aggregate(Sum('amount'))
>>> Money.objects.filter(currency_id='BYN').aggregate(Avg('amount'))
"""