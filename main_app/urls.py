from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('footballers/', views.football_index, name='index'),
    path('footballers/<int:player_id>', views.player_detail, name='player'),
    path('footballers/create', views.EnterPlayer.as_view(), name='enter_player'),
    path('footballers/<int:pk>/update/', views.UpdatePlayer.as_view(), name='update_player'),
    path('footballers/<int:pk>/delete/', views.DeletePlayer.as_view(), name='delete_player'),
    path('footballers/<int:player_id>/add_wage/', views.add_wage, name='add_wage'),
    
    path('trophies/', views.TrophyList.as_view(), name='trophies_index'),
    path('trophies/<int:pk>/', views.TrophyDetail.as_view(), name='trophies_detail'),
    path('trophies/create/', views.TrophyCreate.as_view(), name='trophies_create'),
    path('trophies/<int:pk>/update/', views.TrophyUpdate.as_view(), name='trophies_update'),
    path('trophies/<int:pk>/delete/', views.TrophyDelete.as_view(), name='trophies_delete'),
    path('footballers/<int:player_id>/add_title/<int:trophy_id>/', views.add_title, name='add_title'),
]