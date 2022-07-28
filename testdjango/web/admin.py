from django.contrib import admin

# Register your models here.
from web.models import Site, SiteHistory


# como se va a ver la lista en el admin
class SiteHistoryInline(admin.TabularInline):
    model = SiteHistory
    readonly_fields = ('status_code', 'error_response_content', 'create_at')

    # para no agregar y para no eliminar 
    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'status', 'create_at', 'update_at')
    # convertir parametros en links
    list_display_links = ('id', 'name')
    list_filter = ('status',)
    search_fields = ('id', 'name', 'url')
    # convierte estos params en no editables
    readonly_fields = ('status', 'create_at', 'update_at')
    # orden
    ordering = ('-update_at',)
    # exclude() ayuda aquitar un param
    #agregar otro modelo que se conecta con este
    inlines = (SiteHistoryInline,)


admin.site.register(Site, SiteModelAdmin)
