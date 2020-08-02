from django.db import models
import requests

# TODO: do not judge me for this being a mess now, I'm working on it
# Create your models here.
class SiteInstance:
    def __init__(self, date, site):
        self.site = site
        self.date = self.date_validator(date)

    @staticmethod
    def date_validator(self, date):
        return 'gg'


class SiteInstance():
    """ooo"""
    def __init__(self, site):
        self.site = site

    def collect(self, date):
        """Returns a list of all archived sites from a day"""
        r = requests.get(f'https://web.archive.org/__wb/calendarcaptures/2?url={self.site}&date={date}')
        return r.json()['items']

    def get_site(self, date, site=0):
        site_info = self.collect(date)[site]
        return self.get_url(site_info, date, self.site)

    def get_url(self, site_info, date):
        return f'https://web.archive.org/web/{date}{site_info[0]}/http://{self.site}'