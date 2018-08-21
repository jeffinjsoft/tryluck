# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.

from . import models

@login_required(login_url='/login/')
def index(request):
    lucks = models.Luck.objects.all()
    return render(request, "lucks/index.html", {'lucks':lucks})



@login_required(login_url='/login/')
def mylucks(request):
    lucks = models.Luck.objects.filter(user=request.user)
    return render(request, "lucks/mylucks.html", {'lucks':lucks})
