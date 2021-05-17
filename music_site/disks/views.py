from django.shortcuts import render, get_object_or_404
from .models import Album, Artist, Track
from .forms import SearchForm


def list_albums(request):
    """ Displays a list of all all albums """
    albums = Album.objects.all()

    return render(request, 'disks/albums_list.html', locals())


def album_info(request, id):
    """ Displays all tracks of an album """
    album = get_object_or_404(Album, id=id)
    tracks = Track.objects.filter(album=album)
    tracks = [(track, track.milliseconds//60000, (track.milliseconds % 60000)//1000) for track in tracks]
    return render(request, 'disks/album_info.html', locals())


def search_result(request):
    """ Displays the result of a search on album title """
    #search_key = request.GET['query']
    form = SearchForm(request.POST or None)
    if form.is_valid():
        search_key = form.cleaned_data['search_key']
        albums = Album.objects.filter(title__contains=search_key)
    return render(request, 'disks/search_result.html', locals())
