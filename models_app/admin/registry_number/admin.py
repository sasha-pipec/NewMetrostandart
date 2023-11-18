from django.contrib import admin

from models_app.models import RegistryNumber


@admin.register(RegistryNumber)
class RegistryNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)
    list_per_page = 40
    list_max_show_all = 100
    show_full_result_count = True
