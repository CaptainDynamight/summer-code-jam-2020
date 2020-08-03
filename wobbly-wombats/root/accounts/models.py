from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Username and password are required. Other fields are optional.
    """

    image = models.ImageField(
        upload_to='images/users',
        verbose_name="Image of a user",
        blank=True
    )
    points = models.PositiveIntegerField(default=0, verbose_name="Points gained")

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'






