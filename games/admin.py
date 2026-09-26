from django.contrib import admin
from unfold.admin import ModelAdmin

from games.models import Game


@admin.register(Game)
class GameAdmin(ModelAdmin):
    list_display = [
        "name",
        "publisher",
        "release_date",
        "rating",
    ]

    search_fields = [
        "name",
        "description",
        "publisher__name",
    ]

    list_filter = [
        "publisher",
        "genres",
        "release_date",
    ]

    list_select_related = [
        "publisher",
    ]

    filter_horizontal = [
        "genres",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]
