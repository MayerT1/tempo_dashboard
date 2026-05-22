from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_view, name='map'),
    path('api/markers/', views.map_markers_api, name='markers-api'),
]
