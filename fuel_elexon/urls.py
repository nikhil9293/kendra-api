from django.urls import path, include
from rest_framework import routers
from . import views

fuelRouter = routers.DefaultRouter()
fuelRouter.register(r'fuel', views.fuelViewSet)

app_name = 'fuel_elexon'
urlpatterns = [
    path('', include(fuelRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
