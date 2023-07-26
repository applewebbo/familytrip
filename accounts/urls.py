from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("profile/", views.account_profile, name="profile"),
]

htmx_urlpatterns = [
    path("profile/edit/<int:pk>", views.profile_edit, name="profile_edit"),
]

urlpatterns += htmx_urlpatterns
