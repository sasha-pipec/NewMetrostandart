from django.contrib import admin

from models_app.models import Protocol


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    search_fields = ('name', )
