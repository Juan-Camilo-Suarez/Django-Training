from django.contrib import admin, messages

# Register your models here.
from web.models import Site, SiteHistory

# como se va a ver la lista en el admin
from web.services import check_sites


class SiteHistoryInline(admin.TabularInline):
    model = SiteHistory
    readonly_fields = ('status_code', 'error_response_content', 'create_at')

    # para no agregar y para no eliminar
    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# my filter custom
class HttpsFilter(admin.SimpleListFilter):
    title = 'Protocol Sites'
    parameter_name = 'https'

    def has_output(self):
        return True

    def lookups(self, request, model_admin):
        return (
            (True, 'with HTTPS'),
            (False, 'Without HTTPS')
        )

    def queryset(self, request, queryset):
        qs = queryset

        if self.value():
            if self.value() == str(True):
                qs = qs.filter(url__startswith='https://')
            elif self.value() == str(False):
                qs = qs.filter(url__startswith='http://')
        return qs


def check_sites_action(modeladmin, request, queryset):
    site_ids = queryset.values_list('id', flat=True)
    if len(site_ids) > 0:
        check_sites(site_ids)
        modeladmin.message_user(
            request,
            f'{len(site_ids)} sites update.',
            messages.SUCCESS
        )


class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('get_site_full_name', 'id', 'name', 'url', 'status', 'create_at', 'update_at')
    # convertir parametros en links
    list_display_links = ('get_site_full_name', 'id', 'name')
    list_filter = ('status', 'update_at', HttpsFilter)
    search_fields = ('id', 'name', 'url')
    # convierte estos params en no editables
    readonly_fields = ('status', 'create_at', 'update_at')
    # orden
    ordering = ('-update_at',)
    # exclude() ayuda aquitar un param
    # agregar otro modelo que se conecta con este
    inlines = (SiteHistoryInline,)

    # acciones
    actions = (check_sites_action,)
    check_sites_action.short_description = 'update sites'

    # atributos personalisados
    def get_site_full_name(self, instance):
        return f'#{instance.id} {instance.name} ({instance.url})'

    get_site_full_name.short_description = 'complete name site'

    # agregar estilos al admin
    class Media:
        css = {
            'all': ('web/admin.css',)
        }


admin.site.register(Site, SiteModelAdmin)
