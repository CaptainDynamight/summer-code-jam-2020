import random
from .data import adjectives
from .models import PopularSite


def gen_site_url():
    """Returns a dict of url of a page at random interval and the year it was developed"""
    random_key = random.choice(PopularSite.objects.values_list('id', flat=True))
    site = PopularSite.objects.get(id=random_key)
    year = str(random.randint(site.year, 2012))
    date = year + str(random.randint(1, 12)) + str(random.randint(1, 28))
    snapshot = random.randint(100000, 999999)
    return {"url": f'https://web.archive.org/web/{date}{snapshot}/{site.url}',
            "year": year}


def gen_adjective():
    return random.choice(adjectives.ADJECTIVES)
