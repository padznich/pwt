from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Players(models.Model):

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=40)
    coockies_count = models.IntegerField
    created = models.DateTimeField