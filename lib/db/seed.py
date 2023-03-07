# from random import random, randrange, randint, choice as rc

import ipdb

import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import KyleItem

superpowers = [
    "Annoyance Inducement",
    "Cheese Manipulation",
    "Balloon Mimicry",
    "Stench Generation",
    "Matter Ingestion",
    "Enhanced Thievery",
    "Grass Doesn't Grow",
    "Supernatural Fruit Empowerment",
    "Goo Generation",
    "Induce Tickling",
    "Offspring Detection",
    "Morph Hair Color",
    "Fit All Clothes",
    "Footprints Random Shape"
]

engine = create_engine('sqlite:///kyle.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

def make_kyle_items():
    session.query(KyleItem).delete()
    session.commit()

    kyle_items = [KyleItem(
        first_name = "Kyle",
        last_name = fake.last_name(),
        height = round(random.uniform(4.5, 6.5), 2),
        weight = round(random.uniform(100, 200), 1),
        superpower = random.choice(superpowers)
    ) for k in range(15)]
    session.add_all(kyle_items)
    session.commit()

    return kyle_items



if __name__ == '__main__':
    kyle_items = make_kyle_items()

    ipdb.set_trace()






