"""kendra_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
# # from rest_framework import routers
# from carbon_intensity import urls as carbon_urls
# from demand_elexon import views as demand_urls

# # router = routers.DefaultRouter()
# # router.register(r'intensity', carbon_views.IntensityViewSet)
# # router.register(r'demand', demand_views.DemandViewSet)



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('apiv1/', include(carbon_urls)),
#     path('apiv2/', include(demand_urls))
# ]

# from kendra_api.carbon_intensity import urls
# from kendra_api import freq_elexon
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('carbon_intensity.urls')),
    path('api/', include('demand_elexon.urls')),
    path('api/', include('freq_elexon.urls')),
    path('api/', include('fuel_elexon.urls')),
    path('api/', include('price_elexon.urls')),
    path('api/', include('solar.urls')),
    path('api/', include('transmit_elexon.urls')),
    path('api/', include('wind_offshore.urls')),
    path('api/', include('wind_onshore.urls')),
    path('admin/', admin.site.urls)
]
