from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('footballers/', views.football_index, name='index'),
    path('footballers/<int:player_id>', views.player_detail, name='player'),
]