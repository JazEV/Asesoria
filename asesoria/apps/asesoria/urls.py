from django.urls import include, path
from rest_framework import routers
from .views import (
	Turno,
)

router.register('turnos', TurnoViewSet)

urlpatterns = [
	path('', include(router.urls))
	path('turno/create/', include(router.urls))
]
