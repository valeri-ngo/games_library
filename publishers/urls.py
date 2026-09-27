from django.urls import include, path

from publishers.views import (
    create_publisher,
    delete_publisher,
    edit_publisher,
    publisher_details,
    publishers_list,
)

app_name = "publishers"

publishers_urls = [
    path("", view=publisher_details, name="publisher-details"),
    path("edit/", view=edit_publisher, name="edit-publisher"),
    path("delete/", view=delete_publisher, name="delete-publisher"),
]

urlpatterns = [
    path("", view=publishers_list, name="publishers-list"),
    path("create-publisher/", view=create_publisher, name="publisher-create"),
    path("<int:pk>/", include(publishers_urls)),
]
