from rest_framework import viewsets
from .models import Screening
from .serializers import ScreeningSerializer


class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.filter(is_active=True)
    serializer_class = ScreeningSerializer