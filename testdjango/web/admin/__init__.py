from django.contrib import admin

from web.admin.sites import SiteModelAdmin
from web.admin.user import UserModelAdmin
from web.models import Site, User

admin.site.register(Site, SiteModelAdmin)
admin.site.register(User, UserModelAdmin)

