from django.urls import path, include
from rest_framework import routers
from . import views

frequencyRouter = routers.DefaultRouter()
frequencyRouter.register(r'frequency', views.freqViewSet)

app_name = 'freq_elexon'
urlpatterns = [
    path('', include(frequencyRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]