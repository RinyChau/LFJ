from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='access', null=False)
    eth_addr = models.CharField(max_length=512, null=False, blank=False)
    port = models.IntegerField(default=0)
    rpcport = models.IntegerField(default=0)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')


# admin.site.register(User)


