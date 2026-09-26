from django.contrib import admin
from unfold.admin import ModelAdmin

from genres.models import Genre


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = [
        "name",
        "description",
        "created_at",
    ]

    search_fields = [
        "name",
        "description",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]
