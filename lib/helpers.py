from db.models import Base, KyleItem, KyleLog, KyleCart
from prettytable import PrettyTable

YES = ['y', 'ye', 'yes', 'sure', 'i guess']
NO = ['n', 'no']

def create_table(kyles):
    table = PrettyTable()
    table.title = 'Kyles Up For Adoption'
    table.field_names = ['id', 'name', 'superpower']

    for kyle in kyles:
        table.add_row([kyle.id, kyle.last_name, kyle.superpower])
    
    print(table)


def fill_kyle_cart(session):
    # session.query(KyleCart).delete()
    kyles = session.query(KyleItem)
    kyle_item_id = input("Enter ID of the Kyle you would like to adopt: ")
    while kyle_item_id:
        kyle_cart = session.query(KyleCart)
        kyle_cart_all = kyle_cart.all()
        kyle_cart_ids = [c.kyle_id for c in kyle_cart_all]
        kyle_item = session.query(KyleItem).filter(
            KyleItem.id == kyle_item_id).first()
        if kyle_item in kyles:
            new_cart_item = KyleCart(kyle_id=kyle_item_id)
            session.add(new_cart_item)
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














