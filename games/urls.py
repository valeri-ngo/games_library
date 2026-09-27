from django.urls import include, path

from games.views import create_game, delete_game, edit_game, game_details, games_list

app_name = "games"

game_urls = [
    path("", view=game_details, name="game-details"),
    path("edit/", view=edit_game, name="edit-game"),
    path("delete/", view=delete_game, name="delete-game"),
]

urlpatterns = [
    path("", view=games_list, name="games-list"),
    path("create/", view=create_game, name="game-create"),
    path("<int:pk>/", include(game_urls)),
]
