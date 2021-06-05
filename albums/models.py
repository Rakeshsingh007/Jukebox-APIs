from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
import uuid



class MusicAlbums(models.Model):

    GENRECHOICES = (
        ("CM", "Country music"),
        ("EM", "Electronic music"),
        ("RM", "Rock music"),
        ("HM", "Hip hop music"),
        ("LM", "Latin music"),
        ("PM", "Pop music"),
    )

    album_token = models.UUIDField(default=uuid.uuid4,unique=True)
    album_name = models.CharField(max_length=100, validators=[MinLengthValidator(5, message='Album Name should be minimum 5 characters')])
    album_release_date = models.DateField()
    album_genre = models.CharField(max_length=2, choices=GENRECHOICES)
    album_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(100),MaxValueValidator(1000)])
    album_description = models.TextField(null=True, blank= True)
    album_musicians = models.ManyToManyField('musicians.Musicians', blank=True)

    class Meta:
        verbose_name = "Music Album"
        verbose_name_plural = "Music Albums"

    def __str__(self):
        return self.album_name
