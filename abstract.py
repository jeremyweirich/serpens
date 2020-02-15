import re

import requests
from lxml import html


def build_sample(n=10):
    r = requests.get(r"https://en.wikipedia.org/wiki/List_of_proper_names_of_stars")
    r.raise_for_status()
    root = html.fromstring(r.content)
    stars = [
        re.sub(r"[^a-zA-Z ]", "", i.text).title().replace(" ", "")
        for i in root.findall(r".//table[2]//tr/td[3]")
        if i.text
    ]
    print(stars)


if __name__ == "__main__":
    build_sample()
