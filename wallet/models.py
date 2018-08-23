# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True,max_length=50)
    number = models.CharField(blank=True,max_length=50)
    address = models.CharField(blank=True,max_length=50)
    ex_month = models.CharField(blank=True,max_length=50)
    ex_year = models.CharField(blank=True,max_length=50)
    cvv = models.CharField(blank=True,max_length=5)

    user = models.ForeignKey(User)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
       return self.name




class Walet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,unique=True)
    balance = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    due = models.IntegerField(default=0)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return str(self.balance)
