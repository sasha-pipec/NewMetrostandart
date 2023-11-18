from django.contrib import admin

from models_app.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    autocomplete_fields = ('registry_number', 'type')
    list_display = ('name', 'registry_number', 'type')
    list_filter = ('name',)
    search_fields = ('name', 'registry_number__number', 'type__name')
    list_per_page = 40
    list_max_show_all = 100
    show_full_result_count = True
