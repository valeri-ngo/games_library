from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from common.models import CommonModel


def current_year():
    return timezone.localdate().year


class Publisher(CommonModel):
    country = models.CharField(
        max_length=100,
        blank=True,
    )

    founded_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(current_year),
        ],
    )

    website = models.URLField(
        blank=True,
    )
