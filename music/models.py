from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

class Ruta(models.Model):
    city = models.ForeignKey(Song, on_delete=models.CASCADE)
    ruta_name = models.CharField(max_length=250)
    ruta_price = models.CharField(max_length=250)
    ruta_map = models.URLField(blank="True", null="True")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.ruta_name