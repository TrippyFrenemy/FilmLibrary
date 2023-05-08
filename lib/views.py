from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Film

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
    try:
        film = Film.objects.get(category__slug=category_slug, slug=film_slug)
    except Exception as ex:
        raise ex
    return render(request, "film.html", dict(
        film=film
    ))


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            film = Film.objects.get(name=searched)
            return film_detail(request, film.category.slug, film.slug)
        except Exception as ex:
            print(ex)
    return home(request)

