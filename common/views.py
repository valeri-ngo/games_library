from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from games.models import Game


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page with the latest games."""
    latest_games = Game.objects.order_by("-created_at")[:3]

    context = {
        "latest_games": latest_games,
    }

    return render(request, "common/home.html", context)


def custom_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """Render the custom page-not-found response."""
    return render(request, "404.html", status=404)


def custom_500(request: HttpRequest) -> HttpResponse:
    """Render the custom internal-server-error response."""
    return render(request, "500.html", status=500)