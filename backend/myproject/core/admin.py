from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

admin.site.disable_action('delete_selected')


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'is_staff', 'custom_group')

    if not settings.DEBUG:
        def has_delete_permission(self, request, obj=None):
            return False

    def custom_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''
    custom_group.short_description = 'Grupo'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
if not settings.DEBUG:
    admin.site.unregister(Group)
