from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from profiles.validators import UserNameValidator


class Profile(models.Model):
    username = models.CharField(validators=[MinLengthValidator(2),
                                            MaxLengthValidator(15),
                                            UserNameValidator],)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True,
                                      blank=True)