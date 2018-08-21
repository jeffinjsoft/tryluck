# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError

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


@login_required(login_url='/login/')
def addnewlucks(request):
    search = models.Search.objects.all()
    return render(request, "lucks/addnewlucks.html", {'search':search})


@login_required(login_url='/login/')
def lucks_view(request,l_id):

    l = models.Luck.objects.get(pk=l_id)
    print l.status
    return render(request, "lucks/view.html", {'luck':l})

@login_required(login_url='/login/')
def lucks_add_new(request):
    if request.method == "POST":

        s = models.Search.objects.get(name=request.POST['searchvalue'])

        try:
            l = models.Luck()
            l.name = request.POST['name']
            l.content = request.POST['content']
            l.heads = request.POST['heads']
            l.tails = request.POST['tails']
            l.search = s
            l.user = request.user
            l.save()
            messages.success(request, 'Successfully added the luck..')
        except IntegrityError as e:
            messages.warning(request, 'Please use another names')
            return HttpResponseRedirect("/lucks/addnew")
        except Exception as e:
            print e
            messages.warning(request, 'Error in adding')

        return HttpResponseRedirect("/lucks/my")
