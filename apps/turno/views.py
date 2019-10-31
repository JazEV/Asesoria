from rest_framework import viewsets
from .serializers import (
	TurnoSerializer,
)
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
	Turno,
)

class TurnoViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

class TurnoCreate(CreateView):
	model = Turno
	fields = ['nombre', 'apellido', 'horario', 'motivo', 'nota']
	template_name = 'turno/index.html'
	success_url = reverse_lazy('turno:turno_create')
