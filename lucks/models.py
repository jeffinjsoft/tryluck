# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

# Create your models here.


class Search(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.name




class Luck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    content = models.CharField(max_length=5000)
    head=models.CharField(max_length=50)
    tails=models.CharField(max_length=50)
    search = models.ForeignKey(Search)
    duration = models.DateTimeField()
    amount = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    status=models.CharField(max_length=50,default='open')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.name

class Like(models.Model):
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(User)
   luck = models.ForeignKey(Luck)
   option = models.CharField(max_length=10)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __unicode__(self):
      return self.luck.name


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=5000)
    user = models.ForeignKey(User)
    status=models.CharField(max_length=50,default='active')
    luck = models.ForeignKey(Luck)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.status
