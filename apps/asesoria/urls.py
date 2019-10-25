from django.urls import include, path
from rest_framework import viewsets
from rest_framework import routers
from .views import (
	TurnoViewSet,
	TurnoCreate,
	IndexView,
)

router = routers.DefaultRouter()
router.register('turno', TurnoViewSet),


urlpatterns = [
	path('', include(router.urls)),
	path ('turno/create/', TurnoCreate.as_view(), name='turno'),
	path ('turno/index/', IndexView.as_view(), name='index'),
]
