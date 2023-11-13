from django.contrib import admin

from models_app.models import Painting


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    ...
