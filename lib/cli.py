from db.models import Base, KyleItem, KyleLog
import random
from helpers import create_table, fill_kyle_cart

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/kyle.db')
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

    #check if name is kyle, if not raise exception
    name = input('Please enter your first and last name: ')
    [first_name, last_name] = name.split(' ')
    if not (first_name.lower() == 'kyle'):
        raise Exception('We cannot permit the sale of Kyle orphans to individuals not named Kyle.')
    
    #display list of KyleItems
    print(f"Welcome {name} take a look at our merchandise")
    kyles = session.query(KyleItem)
   
    create_table(kyles)
    
    fill_kyle_cart(session, "kyle")

        
    #display information for the kyle selected
    # print('Here is some more information on the Kyle you selected:')
    # print(kyle)    
    # print("Would you like to continue shopping for Kyles?")
     

    






