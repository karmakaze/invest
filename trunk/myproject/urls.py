from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Uncomment this for admin:
    (r'^invest/admin/', include('django.contrib.admin.urls')),

    # Example:
    (r'^invest/', include('myproject.invest.urls')),

)
