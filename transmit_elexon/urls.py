from django.urls import path, include
from rest_framework import routers
from . import views

transmitRouter = routers.DefaultRouter()
transmitRouter.register(r'transmit', views.TransmitViewSet)

app_name = 'transmit_elexon'
urlpatterns = [
    path('', include(transmitRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]