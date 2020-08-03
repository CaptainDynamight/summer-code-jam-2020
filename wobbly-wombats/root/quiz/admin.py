from django.contrib import admin
from .models import Quiz, Site, PopularSite

admin.site.register(Quiz)
admin.site.register(Site)
admin.site.register(PopularSite)