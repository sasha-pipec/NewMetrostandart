from django.contrib import admin

from models_app.models import Subtype


@admin.register(Subtype)
class SubtypeAdmin(admin.ModelAdmin):
    ...
