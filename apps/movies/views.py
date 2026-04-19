from django.shortcuts import render

from rest_framework import viewsets
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """CRUD completo para géneros."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """CRUD completo para películas."""

    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer