from django.urls import include, path
from rest_framework import viewsets
from rest_framework import routers
from .views import (
	TurnoViewSet,
	TurnoCreate,
)

router = routers.DefaultRouter()
router.register('turno', TurnoViewSet)


urlpatterns = [
	path('', include(router.urls)),	
	path ('index/', TurnoCreate.as_view(), name='turno_create'),
]
