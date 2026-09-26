from django.contrib import admin
from unfold.admin import ModelAdmin

from publishers.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(ModelAdmin):
    list_display = [
        "name",
        "country",
        "founded_year",
        "website",
    ]

    search_fields = [
        "name",
        "country",
    ]

    list_filter = [
        "country",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
    ]
