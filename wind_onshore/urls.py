from django.urls import path, include
from rest_framework import routers
from . import views

windOnRouter = routers.DefaultRouter()
windOnRouter.register(r'wind_on', views.WindonViewSet)

app_name = 'wind_onshore'
urlpatterns = [
    path('', include(windOnRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]