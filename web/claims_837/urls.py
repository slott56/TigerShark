#!/usr/bin/env python
"""claims_837.urls

There two RESTful URL's here.  They work in JSON notation.

-   :samp:`load/` is the load service.  This requires a number of parameters.
    See :func:`web.claims_837.views.load`.
    
-   :samp:`{claim_id}/` is the fetch service.  See :func:`web.claims_837.views.fetch`.

"""
from django.conf.urls.defaults import *

urlpatterns = patterns('web.claims_837.views',
    (r'^load/$', 'load'),
    (r'^(?P<claim_id>.*?)/$', 'fetch'),
    (r'^$', 'home'),
)
