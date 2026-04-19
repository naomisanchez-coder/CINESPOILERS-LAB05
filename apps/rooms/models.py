from django.db import models


class Room(models.Model):
    """Sala de cine."""

    class RoomType(models.TextChoices):
        STANDARD = "standard", "Estándar"
        VIP = "vip", "VIP"
        IMAX = "imax", "IMAX"

    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    room_type = models.CharField(
        max_length=20,
        choices=RoomType.choices,
        default=RoomType.STANDARD,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.room_type})"