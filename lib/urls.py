from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:category_slug>",  views.home, name="films_by_category"),
    path("category/<slug:category_slug>/<slug:film_slug>",  views.film_detail, name="film_detail"),
    path("search/",  views.search, name="search"),
    path("about/", views.about, name="about"),
]
