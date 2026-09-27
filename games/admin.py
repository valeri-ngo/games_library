from django.contrib import admin
from unfold.admin import ModelAdmin

from games.models import Game


@admin.register(Game)
class GameAdmin(ModelAdmin):
    list_display: list[str] = [
        "name",
        "publisher",
        "release_date",
        "rating",
    ]

    search_fields: list[str] = [
        "name",
        "description",
        "publisher__name",
    ]

    list_filter: list[str] = [
        "publisher",
        "genres",
        "release_date",
    ]

    list_select_related: list[str] = [
        "publisher",
    ]

    filter_horizontal: list[str] = [
        "genres",
    ]

    readonly_fields: list[str] = [
        "created_at",
        "updated_at",
    ]
