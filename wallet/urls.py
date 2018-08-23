from django.conf.urls import url,include

from . import views



urlpatterns = [
    url(r'^$', views.index,name='wallet'),
    url(r'add/$', views.add,name='addwallet'),

]
