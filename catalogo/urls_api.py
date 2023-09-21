from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsapi import *

router = DefaultRouter()
router.register(r'pais', PaisViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'municipio', MunicipioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]