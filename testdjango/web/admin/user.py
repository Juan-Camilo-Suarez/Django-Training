from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class UserModelAdmin(UserAdmin):
    ordering = ('-create_at',)
    list_display = ('id', 'email', 'is_superuser', 'create_at')
    list_filter = ('is_superuser', 'create_at')
    search_fields = ('id', 'email')
    #espacios del modelo que se pueden editar
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
