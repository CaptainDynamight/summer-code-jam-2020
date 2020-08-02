from django.contrib import admin
from .models import SiteModel

@admin.register(SiteModel)
class SiteAdmin(admin.ModelAdmin):
    fields = ('site', 'date')
    list_display = ('site', 'date', 'url')
