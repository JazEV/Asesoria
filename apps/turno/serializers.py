from rest_framework import serializers
from .models import (
	Turno,
)


class TurnoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Turno
		fields = ['nombre', 'apellido', 'horario', 'nota']
