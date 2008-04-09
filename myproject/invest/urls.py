from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, password_change, password_reset 
from myproject.invest.models import Portfolio, Position

info_dict = {
    'queryset': Portfolio.objects.all(),
    }

dvg = 'django.views.generic'

urlpatterns = patterns('',
    (r'^portfolio/$', dvg+'.list_detail.object_list', info_dict),
    (r'^portfolio/(?P<object_id>\d+)/$', dvg+'.list_detail.object_detail',
					 info_dict),
)
