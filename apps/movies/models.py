from django.db import models

class Genre(models.Model):
    """Género cinematográfico (Acción, Drama, Comedia, etc.)"""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Película disponible en el cine."""

    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ["-release_date"]

    def __str__(self):
        return self.title