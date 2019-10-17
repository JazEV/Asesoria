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

	MOTIVO_CHOICES = [
        ('escolar', 'Escolar'),
        ('personal', 'Personal'),
    ]

	
	horario = models.TimeField(
		null=True,
		blank=True,
		help_text='Ingrese el horario que tenga disponible.'
	)

	notas = models.TextField(
		help_text='(*Opcional.)'
	)


	class Meta:
		verbose_name='Turno'
		verbose_name_plural = "Turnos"

	def __str__(self):
		return '%s' % (self.nombre)
