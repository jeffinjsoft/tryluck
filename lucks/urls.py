from django.conf.urls import url,include

from . import views



urlpatterns = [
    url(r'^$', views.index,name='lucks'),
    url(r'my/$', views.mylucks,name='mylucks'),
]
