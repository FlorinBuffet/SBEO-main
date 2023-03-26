from django.contrib import admin
from .models import Event, Location

# Register your models here.


class LocationAdmin (admin.ModelAdmin):
    list_display = ('club', 'name', 'city')
    list_filter = ('is_deleted',)
    search_fields = ('club', 'name', 'city', 'street')


admin.site.register(Location, LocationAdmin)

admin.site.register(Event)
