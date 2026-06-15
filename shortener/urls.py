from django.urls import path

from . import views

app_name = "shortener"

urlpatterns = [
    path("", views.home, name="home"),
    path("links/", views.list_links, name="list"),
    path("<str:code>/", views.redirect_short_url, name="redirect"),
]