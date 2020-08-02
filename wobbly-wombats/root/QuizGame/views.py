from django.shortcuts import render
import requests

# Create your views here.


def grab_site_url(site, date):
    """Returns the url of the first page from the specified day"""
    r = requests.get(f'https://web.archive.org/__wb/calendarcaptures/2?url={site}&date={date}')
    # TODO: handle if there is no sites
    snapshots = r.json()['items']
    site_info = snapshots[0]
    return f'https://web.archive.org/web/{date}{site_info[0]}/{site}'
