from django.db import models
import requests
from datetime import date as date_type


class SiteModel(models.Model):
    """ooo"""
    site = models.URLField(max_length=40)
    date = models.DateField()
    url = models.URLField(max_length=60, blank=True)

    def save(self, *args, **kwargs):
        """..."""
        self.grab_site_url(str(self.date).replace('-', ''))  # TODO: find a better way to format date
        super().save(*args, **kwargs)

    def grab_site_url(self, date):  # TODO: move this to another place
        """Returns the url of the first page from the specified day"""
        r = requests.get(f'https://web.archive.org/__wb/calendarcaptures/2?url={self.site}&date={date}')
        # TODO: handle if there is no sites
        snapshots = r.json()['items']
        site_info = snapshots[0]
        self.url = f'https://web.archive.org/web/{date}{site_info[0]}/{self.site}'

