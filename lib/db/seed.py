from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import KyleItem

engine = create_engine('sqlite:///kyle.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

def make_kyle_items():
    session.query(KyleItem).delete()
    session.commit()

    kyle_items = [KyleItem(
        first_name = "Kyle",
        last_name = fake.last_name()
    )
    for k in range(15)]
    session.add_all(kyle_items)
    session.commit()

    return kyle_items



if __name__ == '__main__':
    kyle_items = make_kyle_items()






