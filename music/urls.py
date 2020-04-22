from django.urls import path

from . import views

urlpatterns = [
  path('', views.list_page, name='list_page'),
#   path('classical/', views.classical_songs, name='classical')
]