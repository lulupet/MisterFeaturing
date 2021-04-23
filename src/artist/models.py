from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Song(models.Model):
    name = models.CharField(max_length=255, unique=True)


class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
