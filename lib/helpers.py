from prettytable import PrettyTable

def create_table(kyles):
    table = PrettyTable()
    table.title = 'Kyles Up For Adoption'
    table.field_names = ['id', 'name', 'superpower']

    for kyle in kyles:
        table.add_row([kyle.id, kyle.last_name, kyle.superpower])
    
    print(table)




