from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^claim/', include('web.claims.urls')),
    (r'^claim_837/', include('web.claims_837.urls')),
    # (r'^/$', include('web.home.urls')), # Fallback app

    # Uncomment this for admin:
    (r'^admin/', include(admin.site.urls)),
)
