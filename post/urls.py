from django.urls import path
from .views import post_list , post_details, create_post,post_update,post_delete
urlpatterns = [
    path("", post_list, name="post_list"),
    path("<int:id>/", post_details, name="post_details"),
    path("create/", create_post, name="create_post"),
    path("update/<int:id>", post_update, name="post_update"),
    path("<int:id>/delete", post_delete, name="post_delete"),
]
