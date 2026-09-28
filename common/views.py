from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from games.models import Game
from genres.models import Genre
from publishers.models import Publisher


def home(request: HttpRequest) -> HttpResponse:
    """Shows the home page with library statistics and latest games."""
    latest_games = (
        Game.objects.select_related("publisher")
        .prefetch_related("genres")
        .order_by("-created_at")[:6]
    )

    games_count = Game.objects.count()

    genres_count = Genre.objects.count()

    publishers_count = Publisher.objects.count()

    context = {
        "latest_games": latest_games,
        "games_count": games_count,
        "genres_count": genres_count,
        "publishers_count": publishers_count,
    }

    return render(request, "common/home.html", context)


def custom_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """Renders the custom page-not-found response."""
    return render(request, "404.html", status=404)


def custom_500(request: HttpRequest) -> HttpResponse:
    """Render the custom page-500"""
    return render(request, "500.html", status=500)
