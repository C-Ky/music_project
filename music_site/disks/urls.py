from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_albums),
    path('albums/<int:id>', views.album_info, name='album_info'),
]
