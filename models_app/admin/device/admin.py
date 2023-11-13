from django.contrib import admin

from models_app.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    ...
