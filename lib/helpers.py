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


def fill_kyle_cart(session, kyle):
    session.query(KyleCart).delete()
    kyles = session.query(KyleItem)
    kyle_item_id = input("Enter ID of the Kyle you would like to adopt: ")
    while kyle_item_id:
        kyle_item = session.query(KyleItem).filter(
            KyleItem.id == kyle_item_id).first()
        if kyle_item in kyles:
            new_cart_item = KyleCart(kyle_id=kyle_item_id)
            session.add(new_cart_item)
            session.commit()
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



def fill_cart(session, store):
    shopping_cart = ShoppingCart(store=store)
    grocery_item_id = input('Please enter the ID of your first item: ')
    cart_total = 0
    while grocery_item_id:
        grocery_item = session.query(GroceryItem).filter(
            GroceryItem.id==grocery_item_id).first()
        if grocery_item in store.grocery_items:
            shopping_cart.grocery_items.append(grocery_item)
            cart_total += grocery_item.price
            print(f'Cart total is now ${cart_total:.2f}\n')
        else:
            grocery_item_id = input('Please enter a valid grocery item ID: ')
            continue

        yes_no = None
        while yes_no not in YES + NO:
            yes_no = input('Would you like to add another item to your cart? (Y/n) ')
            if yes_no.lower() in YES:
                grocery_item_id = input('Please enter the ID of your next item: ')
            elif yes_no.lower() in NO:
                grocery_item_id = None

    return shopping_cart, cart_total
