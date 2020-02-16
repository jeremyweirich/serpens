import os
import random
import re

import requests
from lxml import html


STARS = [
    "Scheddi",
    "RasElasedAustralis",
    "Rana",
    "RijlAlAwwa",
    "Ruchba",
    "Sadatoni",
    "Sinistra",
    "Media",
    "Menkab",
    "Minkar",
    "Murzim",
    "Muscida",
    "NairAlSaif",
    "Nash",
    "Nembus",
    "Okul",
    "Giedi",
    "Girtab",
    "GorgoneaTertia",
    "Haedus",
    "HoedusI",
    "HoedusIi",
    "Kabdhilinan",
    "Kastra",
    "Kuma",
    "Dnoces",
    "Duhr",
    "Elmuthalleth",
    "FumAlSamakah",
    "Gatria",
    "Askella",
    "Asterion",
    "Auva",
    "Azaleh",
    "Baham",
    "Benetnasch",
    "Betria",
    "Chow",
    "DenebDulfim",
    "DenebKaitosSchemali",
    "Dheneb",
    "AlThalimain",
    "AlThalimain",
    "Arich",
    "Armus",
    "AsellusPrimus",
    "AsellusSecundus",
    "AsellusTertius",
    "AlfeccaMeridiana",
    "AlKalbAlRai",
    "Alkurah",
    "AlMinliarAlAsad",
    "Alrai",
    "Alrami",
    "TejatPrior",
    "Thabit",
    "Tyl",
    "Zubenelakrab",
    "Zubenelakribi",
]

CLASS = """class {cname}(object):
    radial_velocity = None
    def __init__(self, constellation):
        self.constellation = constellation

"""
METHODS = [
    """    @staticmethod
    def correct_static_{f}(x):
        return x ** 10

""",
    """    @classmethod
    def correct_cls_{f}(cls):
        return cls.radial_velocity

""",
    """    def correct_instance_{f}(self, x):
        return self.constellation + x

""",
    """    def instance_should_be_cls_{f}(self):
        return self.radial_velocity

""",
    """    @classmethod
    def cls_should_be_static_{f}(self, x):
        return x ** 10

""",
    """    def instance_should_be_static_{f}(self, x):
        return x ** 10

""",
    """    @staticmethod
    def static_should_be_cls_{f}():
        return {cname}.radial_velocity

""",
]


def stars():
    r = requests.get(r"https://en.wikipedia.org/wiki/List_of_proper_names_of_stars")
    r.raise_for_status()
    root = html.fromstring(r.content)
    return [
        # re.sub(r'[^a-zA-Z ]', '', i).title().replace(' ', '')
        re.sub(r"[^a-zA-Z ]", "", i.text).title().replace(" ", "")
        for i in root.findall(r".//table[2]//tr/td[3]")
        if i.text
    ]


def build_sample(dir=r"sample", n=10, classes=2, functions=8):
    """Build a bunch of sample classes by stitching a random combination of methods together"""
    for _ in range(n):
        name = random.choice(STARS)
        sname = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

        src = ""
        for c in range(classes):
            cname = f"{name}{c}"
            src += CLASS.format(cname=cname)
            for f in range(functions):
                src += random.choice(METHODS).format(cname=cname, f=f)
            src += "\n"

        if not os.path.isdir(dir):
            os.mkdir(dir)
        fp = f"{os.path.join(dir, sname)}.py"
        with open(fp, "w") as f:
            f.write(src)


if __name__ == "__main__":
    build_sample()
