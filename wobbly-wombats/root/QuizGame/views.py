from django.shortcuts import render
import requests
import json
import random


def gen_site_url():
    """Returns the url of the first page from the specified day"""

    with open('data/popular_sites.json') as f:
        popular_sites = json.load(f)

    random_key = random.choice(list(popular_sites.keys()))
    site = popular_sites[random_key][0]
    year = str(random.randint(popular_sites[random_key][1], 2012))
    date = year + str(random.randint(1, 12)) + str(random.randint(1, 30))
    snapshot = random.randint(100000, 999999)
    return {"url": f'https://web.archive.org/web/{date}{snapshot}/{site}',
            "solution": year}


print(gen_site_url())
