# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    # lucks = models.Luck.objects.all()
    current = 200
    total = 1200
    return render(request, "wallet/index.html", {'current':current,'total':total})