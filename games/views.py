from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GameForm
from .models import Game


def games_list(request: HttpRequest) -> HttpResponse:
    """Shows all the games in the library."""
    games_list = (
        Game.objects.select_related("publisher").prefetch_related("genres").all()
    )

    context = {
        "games_list": games_list,
    }

    return render(request, "games/games-list.html", context)


def create_game(request: HttpRequest) -> HttpResponse:
    """Creates a game in the database."""
    if request.method == "POST":
        form = GameForm(request.POST)

        if form.is_valid():
            game = form.save()

            return redirect("games:game-details", pk=game.pk)

    else:
        form = GameForm()

    context = {
        "form": form,
    }

    return render(request, "games/game-create.html", context)


def game_details(request: HttpRequest, pk: int) -> HttpResponse:
    """Shows the game details by PK."""
    game = get_object_or_404(Game, pk=pk)

    context = {
        "game": game,
    }

    return render(request, "games/game-details.html", context)


def edit_game(request: HttpRequest, pk: int) -> HttpResponse:
    """Edits the game by PK."""
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        form = GameForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect("games:game-details", pk=game.pk)

    else:
        form = GameForm(instance=game)

    context = {
        "form": form,
        "game": game,
    }

    return render(request, "games/game-edit.html", context)


def delete_game(request: HttpRequest, pk: int) -> HttpResponse:
    """Deletes the game by PK."""
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        game.delete()

        return redirect("games:games-list")

    context = {
        "game": game,
    }

    return render(request, "games/delete-game.html", context)
