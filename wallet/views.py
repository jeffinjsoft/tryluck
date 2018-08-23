# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required


from . import models

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    # lucks = models.Luck.objects.all()
    # wallet = models.Walet.objects.filter(user=request.user)

    try:
        wallet = models.Walet.objects.get(user=request.user)
    except models.Walet.DoesNotExist:
        print 'no wallet'
        wallet = models.Walet.objects.get_or_create(user=request.user)


    wallet = models.Walet.objects.get(user=request.user)
    print wallet
    current = wallet.balance
    total = wallet.total
    return render(request, "wallet/index.html", {'current':current,'total':total})



@login_required(login_url='/login/')
def add(request):
    if request.method == "POST":
        try:
            amt = int(request.POST['amount'])
        except:
            messages.warning(request, 'amount is not interger')
            return HttpResponseRedirect("/wallet")
        try:
            c = models.Card()
            c.name = request.POST['name']
            c.number = request.POST['cardnumber']
            c.adress = request.POST['address']
            c.ex_month = request.POST['month']
            c.ex_year = request.POST['year']
            c.cvv = request.POST['cvv']
            c.user = request.user
            c.save()
            messages.success(request, 'Successfully added the luck..')
        except IntegrityError as e:
            messages.danger(request, 'intergitry error')
            print e
            return HttpResponseRedirect("/wallet")
        except Exception as e:
            print e
            messages.warning(request, 'Error in processing card')
            return HttpResponseRedirect("/wallet")

        try:
            wallet = models.Walet.objects.get(user=request.user)
        except models.Walet.DoesNotExist:
            print 'no wallet'
            wallet = models.Walet.objects.get_or_create(user=request.user)

        try:
            wallet.balance += amt
            wallet.total += amt
            print wallet.balance
            wallet.save()
        except:
            messages.warning(request, "can't add mount to wallet")
            return HttpResponseRedirect("/wallet")

        return HttpResponseRedirect("/wallet")
