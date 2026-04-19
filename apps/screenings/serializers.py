from rest_framework import serializers
from apps.movies.serializers import MovieSerializer
from apps.rooms.serializers import RoomSerializer
from .models import Screening


class ScreeningSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    room = RoomSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=__import__("apps.movies.models", fromlist=["Movie"]).Movie.objects.all(),
        source="movie",
    )
    room_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=__import__("apps.rooms.models", fromlist=["Room"]).Room.objects.all(),
        source="room",
    )

    class Meta:
        model = Screening
        fields = ["id", "movie", "movie_id", "room", "room_id", "start_time", "price", "is_active"]