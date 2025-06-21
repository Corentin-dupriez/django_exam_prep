from django.core.validators import MinValueValidator
from django.db import models

class Album(models.Model):
    class GenreChoices(models.TextChoices):
        POP = 'Pop Music', 'Pop Music'
        JAZZ = 'Jazz Music', 'Jazz Music'
        RB = 'R&B Music', 'R&B Music'
        ROCK = 'Rock Music', 'Rock Music'
        COUNTRY = 'Country Music', 'Country Music'
        DANCE = 'Dance Music', 'Dance Music'
        HIPHOP = 'Hip Hop Music', 'Hip Hop Music'
        OTHER = 'Other', 'Other'

    name = models.CharField(max_length=30,
                            unique=True,)
    artist = models.CharField(max_length=30,)
    genre = models.CharField(max_length=30,
                             choices=GenreChoices.choices,)
    description = models.TextField(null=True,
                                   blank=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0)],)
    owner = models.ForeignKey('profiles.Profile',
                              on_delete=models.CASCADE,
                              related_name='albums',)


