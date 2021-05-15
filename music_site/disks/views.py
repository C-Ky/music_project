from django.shortcuts import render
from disks.models import Album, Artist, Track


def list_albums(request):
    """ Displays a list of all all albums """
    albums = Album.objects.all()
    return render(request, 'disks/albums_list.html', locals())
