import pandas as pd

def create_table(kyles):
    dtf = pd.DataFrame(columns=['id', 'name', 'superpower'])

    for kyle in kyles:
        dtf.loc[len(dtf.index)] = [kyle.id, kyle.last_name, kyle.superpower]
    
    print(dtf.to_string(index=False))




