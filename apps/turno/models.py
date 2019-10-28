from django.db import models

class Turno(models.Model):
	nombre = models.CharField(
		max_length=20,
		help_text = 'Ingrese su nombre.'
	)

	apellido = models.CharField(
		max_length=20,
		help_text='Ingrese su apellido.'
	)
	
	horario = models.TimeField(
		null=False,
		help_text='Ingrese el horario que tenga disponible.'
	)

	nota = models.TextField(
		blank=True,
		help_text='(*Opcional.)'
	)


	class Meta:
		verbose_name='Turno'
		verbose_name_plural = "Turnos"

	def __str__(self):
		return '%s' % (self.nombre)
