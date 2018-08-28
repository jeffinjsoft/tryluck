from django.conf.urls import url,include

from . import views



urlpatterns = [
    url(r'^$', views.index,name='lucks'),
    url(r'my/$', views.mylucks,name='mylucks'),
    url(r'addnew/$', views.addnewlucks,name='addnewlucks_view'),
    url(r'add/$', views.lucks_add_new,name='addnewlucks'),
    url(r'view/(?P<l_id>[0-9]+)/$', views.lucks_view),
    url(r'del/(?P<l_id>[0-9]+)/$', views.lucks_del),
    url(r'like/(?P<l_id>[0-9]+)/$', views.like),
    url(r'addcomment/$', views.addcomment),
]
