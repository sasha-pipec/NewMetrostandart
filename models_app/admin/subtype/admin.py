from django.contrib import admin

from models_app.models import Subtype


@admin.register(Subtype)
class SubtypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 40
    list_max_show_all = 100
    show_full_result_count = True
