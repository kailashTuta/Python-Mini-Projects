import sqlite3


# Query The DB and Return All Records
def show_all():
    # connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()  # Create a cursor
    c.execute("SELECT rowid,* FROM customers")  # Query The Database
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()  # Commit our command
    conn.close()  # Close our connection


# Add A New Record To The Table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("Insert into customers values(?,?,?)", (first, last, email))
    conn.commit()
    conn.close()


# Add Many Record to Table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("Insert into customers values(?,?,?)", list)
    conn.commit()
    conn.close()


# Delete Record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers where rowid = (?)", id)
    conn.commit()
    conn.close()


# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE email = (?)", (email, ))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()
