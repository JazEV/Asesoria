from rest_framework import viewsets
from .serializers import (
	TurnoSerializer,
)

class TurnoViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer
