from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from genres.forms import GenreForm
from genres.models import Genre


def genres_list(request: HttpRequest) -> HttpResponse:
    """Show all genres."""
    genres = Genre.objects.prefetch_related("games").all()

    context = {
        "genres": genres,
    }

    return render(request, "genres/list-genres.html", context)


def create_genre(request: HttpRequest) -> HttpResponse:
    """Creates a game genre."""
    if request.method == "POST":
        form = GenreForm(request.POST)

        if form.is_valid():
            genre = form.save()

            return redirect("genres:genre-details", pk=genre.pk)

    else:
        form = GenreForm()

    context = {
        "form": form,
    }

    return render(request, "genres/genre-create.html", context)


def genre_details(request: HttpRequest, pk: int) -> HttpResponse:
    """Game genre details by PK."""
    genre = get_object_or_404(Genre.objects.prefetch_related("games"), pk=pk)

    context = {
        "genre": genre,
    }

    return render(request, "genres/genre-details.html", context)


def edit_genre(request: HttpRequest, pk: int) -> HttpResponse:
    """Edits the genre by PK."""
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)

        if form.is_valid():
            form.save()

            return redirect("genres:genre-details", pk=genre.pk)

    else:
        form = GenreForm(instance=genre)

    context = {
        "genre": genre,
        "form": form,
    }

    return render(request, "genres/edit-genre.html", context)


def delete_genre(request: HttpRequest, pk: int) -> HttpResponse:
    """Deletes the genre by PK."""
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == "POST":
        genre.delete()

        return redirect("genres:genres-list")

    context = {
        "genre": genre,
    }

    return render(request, "genres/delete-genre.html", context)
