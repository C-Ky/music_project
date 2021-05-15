from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} by {1}".format(self.title, self.artist)


class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField
    unitPrice = models.DecimalField(max_digits=3, decimal_places=2)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
