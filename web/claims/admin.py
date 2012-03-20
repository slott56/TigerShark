from django.contrib import admin
from web.claims.models import * 

admin.site.register(Location)
admin.site.register(ClaimType)
admin.site.register(SecondaryCoverage)
admin.site.register(Benefit)
admin.site.register(TypeOfService)
admin.site.register(GroupStatus)
admin.site.register(ClaimGroup)
admin.site.register(ClaimProperties)
admin.site.register(X12Message)
admin.site.register(X12Loop)
admin.site.register(X12Segment)

