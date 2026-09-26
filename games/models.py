from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.models import CommonModel


class Game(CommonModel):
    publisher = models.ForeignKey(
        "publishers.Publisher",
        on_delete=models.PROTECT,
        related_name="games",
    )

    genres = models.ManyToManyField(
        "genres.Genre",
        related_name="games",
    )

    release_date = models.DateField(
        blank=True,
        null=True,
    )

    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(
                0.0,
                message="Rating cannot be lower than 0.",
            ),
            MaxValueValidator(
                10.0,
                message="Rating cannot be higher than 10",
            ),
        ],
        null=True,
        blank=True,
    )

    cover_url = models.URLField(
        max_length=500,
        blank=True,
    )
