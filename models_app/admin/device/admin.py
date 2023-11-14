from django.contrib import admin

from models_app.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    search_fields = ('name', 'type__name', 'type__subtype__name')
    list_filter = ('name',)
    filter_horizontal = ('type',)
