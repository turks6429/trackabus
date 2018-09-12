from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Ruta


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

class RutaForm(forms.ModelForm):

    class Meta:
        model = Ruta
        fields = ['ruta_name', 'ruta_price']