from django.db import models

from common.models import CommonModel


class Publisher(CommonModel):
    country = models.CharField(
        max_length=100,
        blank=True,
    )

    founded_year = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
    )
