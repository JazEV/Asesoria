from rest_framework import viewsets

class TurnoPorEscuelaViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

