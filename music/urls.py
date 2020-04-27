from django.urls import path

from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('musician/<int:musician_id>/', views.musician_detail),
  path('music/album/<int:album_id>/', views.album_detail),
  path('music/song/<int:song_id>/', views.song_detail),
]