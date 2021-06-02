from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Musicians(models.Model):

	MUSICIANCHOICES = (
        ("V", "Vocalist"),
        ("I", "Instrumentalist")
    )

    musicians_name = models.CharField(max_length=100, validators=[MinValueValidator(3)])
    musicians_type = models.CharField(choices=MUSICIANCHOICES)
    album_albums = models.ManyToManyField('albums.MusicAlbums')

    class Meta:
        verbose_name = "Musician"
        verbose_name_plural = "Musicians"

    def __str__(self):
        return self.musicians_name
