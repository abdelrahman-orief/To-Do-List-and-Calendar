import sqlite3
import time

# This is our connection to the database
conn = sqlite3.connect('rewarding_system.db')
# This is the cursor. Using it we can add, delete or update information in the database
c = conn.cursor()


def create_table():
    """
    This function creates a table with some columns that will be used later
    """
    c.execute('CREATE TABLE IF NOT EXISTS MyApplication(Name TEXT, Sunday REAL, Monday REAL, Tuesday REAL, '
              'Wednesday REAL, Thursday REAL, Friday REAL, Saturday REAL, Points REAL, '
              'frm_h TEXT, frm_min TEXT, to_h TEXT, to_min TEXT, Date TEXT, Type TEXT, Number REAL, Status REAL)')
    if len(strainer('', 'Type', 'Points'))==0:
        insert_points(0, 'Points')
    if len(strainer('', 'Type', 'Size'))==0:
        insert_size(0, 'Size')
    Date = time.strftime("%d/%m/%Y")
    if len(strainer('', 'Type', 'Date'))==0:
        insert_date(Date, 'Date')
    if strainer('Date', 'Type', 'Date')[0][0]!= Date:
        edit('Date', Date, 'Type', 'Date')
        delete('Type', 'Today')
        edit('status', 0, 'Type', 'Work')
    

def insert_work(name, days, points, frm_h, frm_min, to_h, to_min, Date, Type):
    c.execute("INSERT INTO MyApplication(Name, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, "
              "Points, frm_h, frm_min, to_h, to_min, Date, Type, Status, Number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)",
              (name, days[0], days[1], days[2], days[3], days[4], days[5], days[6], points, frm_h, frm_min, to_h, to_min, Date, Type, int(strainer('Number', 'Type', 'Size')[0][0])))
    edit('Number', int(strainer('Number', 'Type', 'Size')[0][0])+1, 'Type', 'Size')
    conn.commit()
    #insert_work('sun_rep_4_points', [1, 0, 0, 0, 0, 0, 0], 4, 0, 0, 0, 0, '05/11/2017', 'Work')

def insert_reward(name, points, Type):
    c.execute("INSERT INTO MyApplication(Name, Points, Type) VALUES (?, ?, ?)",
              (name, points, Type))
    conn.commit()

def insert_today(name, time, days, points, number):
    c.execute("INSERT INTO MyApplication(Name, frm_h, Sunday, Points, Number, Type) VALUES (?, ?, ?, ?, ?, 'Today')",
              (name, time, days, points, number))
    conn.commit()

def insert_points(points, Type):
    c.execute("INSERT INTO MyApplication(Points, Type) VALUES (?, ?)",
              (points, Type))
    conn.commit()

def insert_size(Size, Type):
    c.execute("INSERT INTO MyApplication(Number, Type) VALUES (?, ?)",
              (Size, Type))
    conn.commit()

def insert_date(Date, Type):
    c.execute("INSERT INTO MyApplication(Date, Type) VALUES (?, ?)",
              (Date, Type))
    conn.commit()

def strainer(select, strain, equals):
    """
    This function works as a strainer. Using it you can get something specific from the database
    :param select: Do you want to get all of the columns or only specific ones?
    :param strain: What should all things you want to see have in common?
    :param equals: What should it be equal to?
    :return a list of what the user wants to see
    """
    # This selects everything if the user didn't enter something for select
    if select == "":
        # Just like adding something, we use the cursor, but instead of INSERT INTO, we write DELETE FROM.
        # WHERE determines which activity the user wants to change
        if strain == "":
            c.execute("SELECT * FROM MyApplication")
            return c.fetchall()
        c.execute("SELECT * FROM MyApplication WHERE {}=(?)".format(strain), [equals])
        return c.fetchall()

    else:
        # Just like adding something, we use the cursor, but instead of INSERT INTO, we write DELETE FROM.
        # WHERE determines which activity the user wants to change
        c.execute("SELECT {} FROM MyApplication WHERE {}=(?)".format(select.upper(), strain), [equals])
        return c.fetchall()

def edit(target, value, strain, equals):
    c.execute('UPDATE MyApplication SET {}=(?) WHERE {}=(?)'.format(target, strain), [value, equals])
    conn.commit()

def delete(target, equals):
    c.execute('DELETE FROM MyApplication WHERE {}=(?)'.format(target), [equals])
    conn.commit()

def delete_today(target, equals):
    c.execute("DELETE FROM MyApplication WHERE {}=(?) AND Type='Today'".format(target), [equals])
    conn.commit()
