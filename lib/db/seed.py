# from random import random, randrange, randint, choice as rc

import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, KyleItem, KyleLog

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
    "Fit No Clothes",
    "Footprints Random Shape"
]

engine = create_engine('sqlite:///kyle.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

if __name__ == '__main__':
    session.query(KyleItem).delete()
    session.query(KyleLog).delete()
    session.commit()

    kyle_items = []
    for _ in range(15):
        kyle_items.append(KyleItem(
        first_name = "Kyle",
        last_name = fake.last_name(),
        height = round(random.uniform(4.5, 6.5), 2),
        weight = round(random.uniform(100, 200), 1),
        superpower = random.choice(superpowers)
        ))

    session.add_all(kyle_items)
    session.commit()

    log_items = []
    for kyle in kyle_items:
        log_items.append(KyleLog(
            kyle_id = kyle.id,
            last_name = kyle.last_name,
            date_of_entry = fake.date()
        ))

    session.add_all(log_items)
    session.commit()






