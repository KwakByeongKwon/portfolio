from django.urls import path
from player_info import views

app_name = 'pitch'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('playerinfo/', views.Player.as_view(), name='player'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('pitching/<int:id>/', views.pitching, name="pitching"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('pitching_avg/<int:id>/', views.pitching_avg, name='pitching_avg'),
    path('vsinfo/<int:id>/', views.vsinfo, name='vsinfo'),
    path('gamedetail/<int:id>/<int:pk>/', views.gamedetail, name='gamedetail'),
    path('delete_opponent/<int:id>/<int:pk>', views.delete_opponent, name='delete_opponent'),
    path('update/<int:pk>/<int:id>/', views.update, name='update'),
    
    
]