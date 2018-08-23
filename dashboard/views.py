# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from lucks.models import Luck

# Create your views here.


def home(request):
    return render(request, "home.html", {})

@login_required(login_url='/login/')
def index(request):
    lucks = Luck.objects.all()
    last_lucks = lucks.order_by('-id')[:5]

    mylucks = Luck.objects.filter(user=request.user)
    last_my_lucks = mylucks.order_by('-id')[:5]

    luckcount = lucks.count()
    mycount = last_my_lucks.count()
    return render(request, "dashboard/index.html", {'luckcount':luckcount,'mycount':mycount,'lucks':last_lucks,'mylucks':last_my_lucks})
