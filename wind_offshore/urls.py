from django.urls import path, include
from rest_framework import routers
from . import views

windOffRouter = routers.DefaultRouter()
windOffRouter.register(r'wind_off', views.WindoffViewSet)

app_name = 'wind_offshore'
urlpatterns = [
    path('', include(windOffRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]