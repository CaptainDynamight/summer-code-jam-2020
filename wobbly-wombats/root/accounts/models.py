from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Username and password are required. Other fields are optional.
    """
    user = models.CharField(max_length=40, unique=True)

    image = models.ImageField(
        upload_to='images/users',
        verbose_name="Image of a user",
        blank=True
    )
    points = models.PositiveIntegerField(default=0, verbose_name="Points gained")
    USERNAME_FIELD = 'user'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
