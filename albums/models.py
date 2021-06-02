from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class MusicAlbums(models.Model):

	GENRECHOICES = (
        ("CM", "Country music"),
        ("EM", "Electronic music"),
        ("RM", "Rock music"),
        ("HM", "Hip hop music"),
        ("LM", "Latin music"),
        ("PM", "Pop music"),
    )

    album_name = models.CharField(max_length=100, validators=[MinValueValidator(5)])
    album_release_date = models.DateField()
    album_genre = models.CharField(choices=GENRECHOICES)
    album_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(100),MaxValueValidator(1000)])
    album_description = models.CharField(null=True, blank= True)
    album_musicians = models.ManyToManyField('musicians.Musicians')

    class Meta:
        verbose_name = "Music Album"
        verbose_name_plural = "Music Albums"

    def __str__(self):
        return self.album_name
