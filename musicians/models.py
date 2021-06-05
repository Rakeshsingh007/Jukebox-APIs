from django.db import models
from django.core.validators import MinLengthValidator
import uuid



class Musicians(models.Model):

    MUSICIANCHOICES = (
        ("V", "Vocalist"),
        ("I", "Instrumentalist")
    )

    musicians_token = models.UUIDField(default=uuid.uuid4,unique=True)
    musicians_name = models.CharField(max_length=100, validators=[MinLengthValidator(3, message='Name should be minimum 3 characters')])
    musicians_type = models.CharField(max_length=2, choices=MUSICIANCHOICES)
    

    class Meta:
        verbose_name = "Musician"
        verbose_name_plural = "Musicians"

    def __str__(self):
        return self.musicians_name
