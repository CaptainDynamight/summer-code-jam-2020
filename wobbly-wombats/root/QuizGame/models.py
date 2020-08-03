from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from .service import gen_site_url, gen_adjective


User = get_user_model()


class PopularSite(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    release_year = models.IntegerField()


class Site(models.Model):
    """Representation of a website, gif, etc. from the exact year"""
    url = models.URLField(verbose_name="Url of a site", blank=True)
    year = models.CharField(max_length=4, verbose_name="Actual year of a site", blank=True)
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.PROTECT,
        verbose_name="Sites for a quiz",
        related_name='sites'
    )

    def save(self, *args, **kwargs):
        if not self.url:
            generated_url = gen_site_url()
            self.url = generated_url['url']
            self.year = generated_url['year']
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.url.split('/')[-1]} from {self.year}"


class Quiz(models.Model):
    """Representation of a quiz"""
    class Category(models.TextChoices):
        WEBSITE = 'websites'
        GIF = 'gifs'
        AUDIO = 'audios'

    user = models.ManyToManyField(
        User,
        verbose_name='Quiz taker',
    )
    category = models.CharField(
        choices=Category.choices,
        default=Category.WEBSITE,
        verbose_name="Category of a quiz",
        max_length=64
    )
    title = models.CharField(max_length=64, verbose_name="Title of the quiz", blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            adjective = gen_adjective()
            self.title = f'{adjective} + quiz!'

        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
