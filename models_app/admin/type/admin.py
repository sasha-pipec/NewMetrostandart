from django.contrib import admin

from models_app.models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    ...
