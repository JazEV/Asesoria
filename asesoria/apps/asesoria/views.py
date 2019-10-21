from rest_framework import viewsets
from .serializers import (
	TurnoSerializer,
)
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
	Turno,
)

class TurnoViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

class PreguntaCreate(LoginRequiredMixin, CreateView):
	model = Turno
	fields = ['nombre', 'apellido', 'motivo', 'horario', 'notas']
	template_name = 'template/turno/create.html'
	success_url = reverse_lazy('turno:index')

class IndexView(LoginRequiredMixin, ListView):
	model = Turno
	template_name = 'templates/turno/index.html'
	context_object_name = 'turnos'