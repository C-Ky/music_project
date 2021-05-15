from django.shortcuts import render, get_object_or_404
from disks.models import Album, Artist, Track


def list_albums(request):
    """ Displays a list of all all albums """
    albums = Album.objects.all()
    return render(request, 'disks/albums_list.html', locals())


def album_info(request, id):
    """ Displays all tracks of an album """
    album = get_object_or_404(Album, id=id)
    tracks = Track.objects.filter(album=album)
    return render(request, 'disks/album_info.html', locals())
