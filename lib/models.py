from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("name", )
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse("films_by_category", args=[self.slug])

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='film', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ("name", )
        verbose_name = "film"
        verbose_name_plural = "films"

    def get_url(self):
        return reverse("film_detail", args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "actor"
        verbose_name_plural = "actors"

    def get_url(self):
        return reverse("actor_detail", args=[self.slug])

    def __str__(self):
        return self.name