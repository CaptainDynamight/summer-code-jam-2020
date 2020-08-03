import json
import random


def gen_site_url():
    """Returns a dict of url of a page at random interval and the year it was developed"""
    with open('QuizGame/data/popular_sites.json') as f:
        popular_sites = json.load(f)

    random_key = random.choice(list(popular_sites.keys()))
    site = popular_sites[random_key][0]
    year = str(random.randint(popular_sites[random_key][1], 2012))
    date = year + str(random.randint(1, 12)) + str(random.randint(1, 30))
    snapshot = random.randint(100000, 999999)
    return {"url": f'https://web.archive.org/web/{date}{snapshot}/{site}',
            "solution": year}
