from django.urls import path, include
from rest_framework import routers
from . import views

demandRouter = routers.DefaultRouter()
demandRouter.register(r'demand', views.DemandViewSet)

app_name = 'demand_elexon'
urlpatterns = [
    path('', include(demandRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]