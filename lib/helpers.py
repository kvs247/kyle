from db.models import Base, KyleItem, KyleLog, KyleCart
from prettytable import PrettyTable
import datetime

YES = ['y', 'ye', 'yes', 'sure', 'i guess']
NO = ['n', 'no']

def create_table(kyles):
    table = PrettyTable()
    table.title = 'Kyles Up For Adoption'
    table.field_names = ['id', 'name', 'superpower', 'height (Kyles)', 'weight (Kyle units)']

    for kyle in kyles:
        table.add_row([
            kyle.id, 
            kyle.first_name + ' ' +  kyle.last_name, 
            kyle.superpower,
            kyle.height,
            kyle.weight
            ])
    
    print(table)


def fill_kyle_cart(session):
    session.query(KyleCart).delete()
    kyles = session.query(KyleItem)
    kyle_item_id = input("Enter ID of the Kyle you would like to adopt: ")
    while kyle_item_id:
        kyle_cart = session.query(KyleCart)
        kyle_cart_all = kyle_cart.all()
        kyle_cart_ids = [c.kyle_id for c in kyle_cart_all]
        kyle_item = session.query(KyleItem).filter(
            KyleItem.id == kyle_item_id).first()
        if kyle_item in kyles:
            now = datetime.date.today()
            # update Kyle Log
            session.query(KyleLog).filter(
                KyleLog.kyle_id == int(kyle_item_id)
                ).first().date_of_adoption = now
            # add Kyle to cart
            new_cart_item = KyleCart(
                kyle_id = kyle_item_id,
                first_name = kyle_item.first_name,
                last_name = kyle_item.last_name,
                superpower = kyle_item.superpower
                )
            session.add(new_cart_item)
            # remove Kyle from List
            session.delete(kyle_item)

            session.commit()
        elif int(kyle_item_id) in kyle_cart_ids:
           kyle_item_id = input(f"You've already added Kyle number {kyle_item_id} to your cart: ")
           continue
        else:
            kyle_item_id = input("We demand you enter a valid ID, motherfucker: ")
            continue

        yes_no = None
        while yes_no not in YES + NO:
            yes_no = input('Would you like to consider subjugating another Kyle? (Y/n) ')
            if yes_no.lower() in YES:
                kyle_item_id = input('Please enter the ID of your next item: ')
            elif yes_no.lower() in NO:
                kyle_item_id = None

def show_kyle_log(session):
    yes_no = input('Would you like to see our Kyle log? (Y/n) ')
    if yes_no.lower() in YES:
        kyle_log = session.query(KyleLog)
        table = PrettyTable()
        table.title = 'Kyles Log'
        table.field_names = ['id', 'name', 'date of entry', 'date of sale']

        for kyle in kyle_log:
            table.add_row([kyle.id, kyle.first_name + ' ' +  kyle.last_name, kyle.date_of_entry, kyle.date_of_adoption])
        
        print(table)

def get_total(session):
    input('Press ENTER to checkout.')
    kyle_cart = session.query(KyleCart)
    table = PrettyTable()
    table.title = 'Cart Total'
    table.field_names = ['id', 'kyle id', 'name', 'superpower']
    total = 0

    for kyle in kyle_cart:
        table.add_row([
            kyle.id, 
            kyle.kyle_id, 
            f'{kyle.first_name} {kyle.last_name}',
            kyle.superpower
            ])
        total += 2

    print(table)
    print(f'Fork over ${total}, nerd')
