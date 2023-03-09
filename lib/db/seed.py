# from random import random, randrange, randint, choice as rc

import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, KyleItem, KyleLog, KyleCart

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
    "Footprints Random Shape",
    "See Through Glass [NJ]",
    "Summon Gaggle of Geese [TH]",
    "Invisble While Motionless [TH]",
    "See Contents of Empty Box [SP]",
    "Win Skribbl (if Steve & Nick absent) [BA]",
    "Eat 1 More Piece of Sushi Than Everyone Else [NJ]",
    "Lose/Regrow All Teeth (ALL teeth) [NJ]",
    "Walk on Legos Without Pain [NJ]",
    "Live Longer Than Louis [TH]",
    "Morph Into Danny Devito [BA]",
    "Fly 2 Inches Off the Ground [TH]",
    "Is Very Handsome [NJ]",
    "Is Really Really Smart [TH]",
    "Fix Games With Breath [NJ]",
    "Win Any Argument But Singing [BA]",
    "Induce Sneezing [AM]",
    "Fly Incredibly Slow [AM]"
]

engine = create_engine('sqlite:///kyle.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

if __name__ == '__main__':
    session.query(KyleItem).delete()
    session.query(KyleLog).delete()
    session.query(KyleCart).delete()
    session.commit()

    kyle_items = []
    for _ in range(31):
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
            first_name = 'Kyle',
            last_name = kyle.last_name,
            date_of_entry = fake.date()
        ))

    session.add_all(log_items)
    session.commit()






