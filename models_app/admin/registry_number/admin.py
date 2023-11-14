from django.contrib import admin

from models_app.models import RegistryNumber


@admin.register(RegistryNumber)
class RegistryNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'device')
    search_fields = ('number', 'device__name',
                     'device__type__name', 'device__type__subtype__name')
    list_filter = ('device','device__type')
