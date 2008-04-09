from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^invest/', include('myproject.invest.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
