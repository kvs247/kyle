# Kyles' Orphanage: Adopt a Kyle Today!

## Introduction
Welcome to Kyles' Orphanage! This orphanage is dedicated to helping Kyles in need, by Kyles for Kyles. This project utilizes several Python libraries such as ipdb, sqlalchemy, alembic, prettytable, and faker to populate a SQL database with information about the orphans at the orphanage. Using the command line interface, users can browse and adopt their very own Kyle(s)!

## Command Line Interface
To visit the orphanage, follow these steps:

1. Initiate the project with `pipenv install` and `pipenv shell`.
2. Populate the SQL database with data from `faker` by running `python seed.py` from the `db` directory.
3. Verify the integrity of the database by checking that `kyle.db` contains a `kyle_items` table populated with data, a `kyle_logs` table populated with the same number of data points as `kyle_items`, and an empty table `kyle_carts`.
4. Run `python cli.py` from the `lib` directory.
5. Follow the prompts on screen to browse and adopt your very own Kyle! (Sale is exclusively reserved to customers who can provide documentation of their first given name being Kyle).

## Helpers.py
The `helpers.py` file provides functionality to the `cli.py` file, reducing the size of the latter.

### create_table
Utilizes `prettytable` to display the `kyle_items` table which contains information about orphans currently staying at the orphanage. It displays the height in units of Kyles and weight in units of Kyle units.

### fill_kyle_cart
Prompts the user to choose a Kyle to adopt and uses `while` loops to adopt multiple Kyles. Dynamically updates the tables as the user selects Kyles to adopt. Pass the SQLAlchemy `session` object into the function so that it can perform database queries.

### show_kyle_log
Prompts the user to select if they would like to view the record of Kyles that have stayed at the orphanage. If desired, prints out the `kyle_logs` table using `prettytable` as in `create_table`.

### get_total
Prints the user's shopping cart and calculates the total.
