from django.shortcuts import render, get_object_or_404
from .models import Category, Film, Actor

# Create your views here.
def home(request, category_slug=None):
    category_page = None
    films = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        films = Film.objects.filter(category=category_page)
    else:
        films = Film.objects.all()

    return render(request, "home.html", dict(
        category=category_page,
        films=films
    ))


def about(request):
    return render(request, "about.html")


def film_detail(request, category_slug=None, film_slug=None):
    pass