from django.db.models import Prefetch
from django.db.models.deletion import ProtectedError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from games.models import Game
from publishers.forms import PublisherForm
from publishers.models import Publisher


def publishers_list(request: HttpRequest) -> HttpResponse:
    """Show all the publishers."""
    list_publishers = Publisher.objects.prefetch_related("games").all()

    context = {
        "list_publishers": list_publishers,
    }

    return render(request, "publishers/publishers-list.html", context)


def create_publisher(request: HttpRequest) -> HttpResponse:
    """Creates a publisher."""
    if request.method == "POST":
        form = PublisherForm(request.POST)

        if form.is_valid():
            publisher = form.save()

            return redirect("publishers:publisher-details", pk=publisher.pk)

    else:
        form = PublisherForm()

    context = {
        "form": form,
    }

    return render(request, "publishers/publisher-create.html", context)


def publisher_details(request: HttpRequest, pk: int) -> HttpResponse:
    """Shows the publisher details by PK."""
    publisher = get_object_or_404(
        Publisher.objects.prefetch_related(
            Prefetch(
                "games",
                queryset=Game.objects.select_related("publisher").prefetch_related(
                    "genres"
                ),
            )
        ),
        pk=pk,
    )

    context = {
        "publisher": publisher,
    }

    return render(request, "publishers/publisher-details.html", context)


def edit_publisher(request: HttpRequest, pk: int) -> HttpResponse:
    """Edits the publisher details by PK."""
    publisher = get_object_or_404(Publisher, pk=pk)

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)

        if form.is_valid():
            form.save()

            return redirect("publishers:publisher-details", pk=publisher.pk)

    else:
        form = PublisherForm(instance=publisher)

    context = {
        "form": form,
        "publisher": publisher,
    }

    return render(request, "publishers/edit-publisher.html", context)


def delete_publisher(request: HttpRequest, pk: int) -> HttpResponse:
    """Deletes the publisher by PK."""
    publisher = get_object_or_404(Publisher, pk=pk)

    if request.method == "POST":
        try:
            publisher.delete()
        except ProtectedError:
            context = {
                "publisher": publisher,
                "deletion_error": (
                    "This publisher cannot be deleted because it has associated games."
                ),
            }

            return render(request, "publishers/delete-publisher.html", context)

        return redirect("publishers:publishers-list")

    context = {
        "publisher": publisher,
    }

    return render(request, "publishers/delete-publisher.html", context)
