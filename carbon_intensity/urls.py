from django.urls import path, include
from rest_framework import routers
from . import views

intensityRouter = routers.DefaultRouter()
intensityRouter.register(r'intensity', views.IntensityViewSet)

app_name = 'carbon_intensity'
urlpatterns = [
    path('', include(intensityRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


