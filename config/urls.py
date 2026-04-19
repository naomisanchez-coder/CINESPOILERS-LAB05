"""
URL configuration for cinespoilers project.
Each app will include its own urls.py here.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Las URLs de cada app se incluirán así:
    # path("api/v1/movies/", include("movies.urls")),
]