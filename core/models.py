from django.db import models
from django.conf import settings

import uuid


class Movie(models.Model):
    GENRE_CHOICES = [
        ("action", "Action"),
        ("comedy", "Comedy"),
        ("drama", "Drama"),
        ("horror", "Horror"),
        ("romance", "Romance"),
        ("science_fiction", "Science_fiction"),
        ("fantasy", "Fantasy"),
    ]

    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to="movie_images/")
    image_cover = models.ImageField(upload_to="movie_images/")
    video = models.FileField(upload_to="movie_images")
    movie_view = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class MovieList(models.Model):
    owner_movie = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
