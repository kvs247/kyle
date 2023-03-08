from db.models import Base, KyleItem, KyleLog
import random
from helpers import create_table

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///kyle.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

if __name__ == '__main__':
    # Welcome to Only Kyles, register your name
    print('''
    =============================================================================
    ░█████╗░███╗░░██╗██╗░░░░░██╗░░░██╗  ██╗░░██╗██╗░░░██╗██╗░░░░░███████╗░██████╗
    ██╔══██╗████╗░██║██║░░░░░╚██╗░██╔╝  ██║░██╔╝╚██╗░██╔╝██║░░░░░██╔════╝██╔════╝
    ██║░░██║██╔██╗██║██║░░░░░░╚████╔╝░  █████═╝░░╚████╔╝░██║░░░░░█████╗░░╚█████╗░
    ██║░░██║██║╚████║██║░░░░░░░╚██╔╝░░  ██╔═██╗░░░╚██╔╝░░██║░░░░░██╔══╝░░░╚═══██╗
    ╚█████╔╝██║░╚███║███████╗░░░██║░░░  ██║░╚██╗░░░██║░░░███████╗███████╗██████╔╝
    ░╚════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░
    =============================================================================
    ''')
    print('Hello! Welcome to Only Kyles, the Kyle orphanage by Kyles that finds Kyles for Kyles.')
    name = input('Please enter your first and last name: ')
    [first_name, last_name] = name.split(' ')
    if not (first_name.lower() == 'kyle'):
        raise Exception('We cannot permit the sale of Kyle orphans to individuals not named Kyle.')
    
    print(f"Welcome {name} take a look at our merchandise")
    kyles = session.query(KyleItem)
    print(kyles.first())
    create_table(kyles)