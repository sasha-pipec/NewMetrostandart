from django.contrib import admin

from models_app.models import DeviceProtocol


@admin.register(DeviceProtocol)
class DeviceProtocolAdmin(admin.ModelAdmin):
    autocomplete_fields = ('device', 'protocol')
