from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Category", max_length=255)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cinema:actor-detail", kwargs={"slug": self.name})


    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"


class Genre(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField("Title", max_length=150)
    tagline = models.CharField("Tagline", max_length=100, default="")
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release date", default=2019)
    country = models.CharField("Country", max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    world_premiere = models.DateField("World Premiere", default=date.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text="Enter the amount in dollars")
    fees_in_usa = models.PositiveIntegerField("US fees", default=0, help_text="Enter the amount in dollars")
    fees_in_world = models.PositiveIntegerField("Fees in the world ", default=0, help_text="Enter the amount in dollars")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cinema:movie-detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShot(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movies_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Film frame"
        verbose_name_plural = "Film stills"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Meaning", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Star rating"
        verbose_name_plural = "Rating Stars"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Text", max_length=5000)
    parent = models.ForeignKey("self",
                               verbose_name="Parent",
                               on_delete=models.SET_NULL,
                               blank=True, null=True,
                               related_name="children")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
