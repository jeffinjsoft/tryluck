# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.db import IntegrityError

from dateutil import parser
import json

from django.contrib.auth.decorators import login_required

from wallet.models import Walet

# Create your views here.

from . import models

@login_required(login_url='/login/')
def index(request):
    lucks = models.Luck.objects.filter(status='open')
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
    comments = models.Comment.objects.filter(luck=l).order_by('-id')[:5]
    h_count = models.Like.objects.filter(luck=l,user=request.user,option='head').count()
    t_count = models.Like.objects.filter(luck=l,user=request.user,option='tail').count()

    return render(request, "lucks/view.html", {'luck':l,'comments':comments,'h_count':h_count,'t_count':t_count})

@login_required(login_url='/login/')
def lucks_del(request,l_id):
    l = models.Luck.objects.get(pk=l_id)
    if l.user == request.user:
        try:
            l.delete()
            messages.success(request, 'Successfully deleted')
        except:
            messages.warning(request, 'Unable to delete')
    return HttpResponseRedirect("/lucks/my/")

@login_required(login_url='/login/')
def lucks_add_new(request):
    if request.method == "POST":

        s = models.Search.objects.get(name=request.POST['searchvalue'])

        # pre checks
        try:
            amt = int(request.POST['amount'])
        except:
            messages.warning(request, 'amount is not interger')
            return HttpResponseRedirect("/lucks/addnew")


        try:
            l = models.Luck()
            l.name = request.POST['name']
            l.content = request.POST['content']
            l.head = request.POST['heads']
            l.tails = request.POST['tails']
            l.search = s
            l.user = request.user
            duration = parser.parse(request.POST.get('duration'))
            l.duration = duration
            l.amount = amt
            l.save()
            messages.success(request, 'Successfully added the luck..')
        except IntegrityError as e:
            messages.warning(request, 'Please use another names')
            print e
            return HttpResponseRedirect("/lucks/addnew")
        except Exception as e:
            print e
            messages.warning(request, 'Error in adding')

        return HttpResponseRedirect("/lucks/my")



@login_required(login_url='/login/')
def addcomment(request):
    if request.method == "POST":
        comment = request.POST.get('the_comment')

        response_data = {}
        try:
            l = models.Luck(pk=request.POST['luck'])
            c = models.Comment(comment=comment, user=request.user,luck=l)
            c.save()

            response_data['result'] = 'success!'
            response_data['html'] = """
                <strong class="pull-left primary-font">"""+request.user.username+"""</strong>
                    <small class="pull-right text-muted">
                       <span class="glyphicon glyphicon-time"></span>...</small>
                    </br>
                    <li class="ui-state-default">"""+comment+""". </li>
                    </br>
            """
        except:
            print 'error!!!!!!!!!!!'
            response_data['result'] = 'cant create comment!'


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )




@login_required(login_url='/login/')
def like(request,l_id):
    if request.user and request.method == "GET":
        vote = request.GET['v']
        l = models.Luck.objects.get(id=l_id)
        w = Walet.objects.get(user=request.user)

        if l.amount < w.balance:
            w.balance -= l.amount

            like = models.Like(user=request.user,luck=l,option=vote)
            like.save()

            w.save()

            messages.success(request, "Successfully chosed")
            return HttpResponseRedirect("/lucks/view/"+l_id+"/")

        else:
            messages.warning(request, "You don't have enough balance. Please add balance")
            return HttpResponseRedirect("/wallet/")


    else:
        return HttpResponseRedirect("/lucks/view/"+l_id+"/")
