from django.urls import include, path

from genres.views import (
    create_genre,
    delete_genre,
    edit_genre,
    genre_details,
    genres_list,
)

app_name = "genres"

genre_urls = [
    path("", view=genre_details, name="genre-details"),
    path("edit/", view=edit_genre, name="genre-edit"),
    path("delete/", view=delete_genre, name="genre-delete"),
]

urlpatterns = [
    path("", view=genres_list, name="genres-list"),
    path("create/", view=create_genre, name="genre-create"),
    path("<int:pk>/", include(genre_urls)),
]
