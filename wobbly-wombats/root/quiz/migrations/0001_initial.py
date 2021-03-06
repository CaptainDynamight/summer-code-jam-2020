# Generated by Django 3.0.9 on 2020-08-03 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('release_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('websites', 'Website'), ('gifs', 'Gif'), ('audios', 'Audio')], default='websites', max_length=64, verbose_name='Category of a quiz')),
                ('title', models.CharField(blank=True, max_length=64, verbose_name='Title of the quiz')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Quiz taker')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, verbose_name='Url of a site')),
                ('year', models.CharField(blank=True, max_length=4, verbose_name='Actual year of a site')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sites', to='quiz.Quiz', verbose_name='Sites for a quiz')),
            ],
        ),
    ]
