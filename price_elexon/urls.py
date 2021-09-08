from django.urls import path, include
from rest_framework import routers
from . import views

PriceRouter = routers.DefaultRouter()
PriceRouter.register(r'price', views.PriceViewSet)

app_name = 'price_elexon'
urlpatterns = [
    path('', include(PriceRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]