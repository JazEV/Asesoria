from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Turno(models.Model):
	nombre = models.CharField(
		max_length=20,
		help_text = 'Ingresá tu nombre.'
	)

	apellido = models.CharField(
		max_length=20,
		help_text='Ingresá tu apellido.'
	)
	
	horario = models.TimeField(
		null=False,
		help_text='Ingresá el horario que te quede cómodo.'
	)

	ESCOLAR = "Escolar"
	PERSONAL = "Personal"

	MOTIVO = [
        (ESCOLAR, 'Escolar'),
        (PERSONAL, 'Personal')
    ]

	motivo = models.CharField(max_length=1, choices=MOTIVO, default=ESCOLAR, help_text='Ingresá el motivo.')

	telefono = PhoneNumberField('Teléfono', help_text='Ingresá tu teléfono.')

	email = models.EmailField(help_text='Ingresá tu email.')

	nota = models.TextField(
		blank=True,
		help_text='Ingresá un resumen del motivo. (*Opcional.)'
	)

	class Meta:
		verbose_name='Turno'
		verbose_name_plural = "Turnos"

	def __str__(self):
		return '%s' % (self.nombre)
