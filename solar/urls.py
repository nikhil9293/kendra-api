from django.urls import path, include
from rest_framework import routers
from . import views

solarRouter = routers.DefaultRouter()
solarRouter.register(r'solar', views.solarViewSet)

app_name = 'solar'
urlpatterns = [
    path('', include(solarRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]