from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Event, Location

# Register your models here.

admin.site.disable_action('delete_selected')


@admin.action(description='Delete Location')
def location_delete(self, request, queryset):
    deleted = queryset.update(is_deleted=True)
    self.message_user(request, ngettext(
        '%d location has been deleted.',
        '%d locations have been deleted.',
        deleted,
    ) % deleted, messages.SUCCESS)


class LocationAdmin (admin.ModelAdmin):
    list_display = ('club', 'name', 'city')
    list_filter = ('is_deleted',)
    actions = [location_delete]
    search_fields = ('club', 'name', 'city', 'street')


admin.site.register(Location, LocationAdmin)

admin.site.register(Event)
