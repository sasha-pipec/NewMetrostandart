from django.contrib import admin

from models_app.models import RegistryNumber


@admin.register(RegistryNumber)
class RegistryNumberAdmin(admin.ModelAdmin):
    ...
