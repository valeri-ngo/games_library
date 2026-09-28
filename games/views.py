from django.db.models import F, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from genres.models import Genre
from publishers.models import Publisher

from .forms import GameDeleteForm, GameForm
from .models import Game


def games_list(request: HttpRequest) -> HttpResponse:
    """Shows all the games in the library."""
    games_list = (
        Game.objects.select_related("publisher").prefetch_related("genres").all()
    )

    search_query = request.GET.get("q", "").strip()
    selected_genre = request.GET.get("genre", "")
    selected_publisher = request.GET.get("publisher", "")
    selected_sort = request.GET.get("sort", "name")

    if search_query:
        games_list = games_list.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )

    if selected_genre.isdigit():
        games_list = games_list.filter(genres__pk=int(selected_genre))

    if selected_publisher.isdigit():
        games_list = games_list.filter(publisher__pk=int(selected_publisher))

    allowed_sorting = {
        "name": "name",
        "-name": "-name",
        "rating": F("rating").asc(nulls_last=True),
        "-rating": F("rating").desc(nulls_last=True),
        "release_date": F("release_date").asc(nulls_last=True),
        "-release_date": F("release_date").desc(nulls_last=True),
    }

    games_list = games_list.order_by(
        allowed_sorting.get(selected_sort, "name")
    ).distinct()

    context = {
        "games_list": games_list,
        "genres": Genre.objects.all(),
        "publishers": Publisher.objects.all(),
        "search_query": search_query,
        "selected_genre": selected_genre,
        "selected_publisher": selected_publisher,
        "selected_sort": selected_sort,
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
    game = get_object_or_404(
        (Game.objects.select_related("publisher").prefetch_related("genres")), pk=pk
    )

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

    form = GameDeleteForm(instance=game)

    context = {
        "game": game,
        "form": form,
    }

    return render(request, "games/delete-game.html", context)
