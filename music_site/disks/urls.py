from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_albums, name='homepage'),
    path('albums/<int:id>', views.album_info, name='album_info'),
    path('albums/search', views.search_result, name='search_result')
]
