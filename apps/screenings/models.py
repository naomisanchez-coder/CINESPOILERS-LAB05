from django.db import models
from apps.movies.models import Movie
from apps.rooms.models import Room


class Screening(models.Model):
    """Función de cine: película + sala + horario."""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="screenings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="screenings")
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Función"
        verbose_name_plural = "Funciones"
        ordering = ["start_time"]

    def __str__(self):
        return f"{self.movie} - {self.room} - {self.start_time}"