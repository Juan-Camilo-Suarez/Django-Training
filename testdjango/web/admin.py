from django.contrib import admin

# Register your models here.
from web.models import Site


# como se va a ver la lista en el admin
class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'status')
    list_display_links = ('id', 'name')


admin.site.register(Site, SiteModelAdmin)
