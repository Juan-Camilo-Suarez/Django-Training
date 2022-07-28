from django.contrib import admin

# Register your models here.
from web.models import Site


# como se va a ver la lista en el admin
class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'status', 'create_at', 'update_at')
    # convertir parametros en links
    list_display_links = ('id', 'name')
    list_filter = ('status',)
    search_fields = ('id', 'name', 'url')
    # convierte estos params en no editables
    readonly_fields = ('status', 'create_at', 'update_at')


admin.site.register(Site, SiteModelAdmin)
