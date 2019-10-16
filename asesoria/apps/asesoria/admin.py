from django.contrib import admin
from .models import (
	Turno,
)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):

	list_filter = ('nombre', 'apellido')
	search_fields = ['nombre__icontains', 'apellido']
	list_display = ('nombre', 'apellido')
