import sqlite3

def sql_connection():
    try:
        db = sqlite3.connect('crud.sqlite')
        return db
    except Exception as e:
        print(e)


def create_table(con):
    """ Create the table with given columns
    """
    try:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT,
        nickname TEXT
                    );
        ''')
        con.commit()
        print('The table is created successfully')
    except Exception as e:
        print(e)

def insert_data(con, entities):
    """  Insert records into the table
    """
    query = """INSERT INTO users (name, nickname, password) VALUES(?,?,?)"""

    try:
        cur = con.cursor()
        cur.execute(query, entities)
        con.commit()
        print("The record added successfully")
    except Exception as e:
        print(e)


""" def add_data(con):
    The second method to add records into the table
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO users(name, password, nickname) VALUES('David', '123', 'david_brazil')")
        cur.execute("INSERT INTO users(name, password, nickname) VALUES('Tom', '444', 'tom_holland_12')")
        cur.execute("INSERT INTO users(name, password, nickname) VALUES('Alan', '542', 'alan_wake_000')")
        cur.execute("INSERT INTO users(name, password, nickname) VALUES('Iago', '2', 'iagomauricioo')")
        con.commit()
        print("The records added successfully")
    except Exception as e:
        print(e) """


def select_all(con):
    """Selects all rows from the table to display
    """
    print("\n")
    try:
        cur = con.cursor()
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def update_data(con, password, id):
    """ Update the table with given new values"""
    try:
        cur = con.cursor()
        cur.execute("UPDATE users SET password = ?  WHERE id = ?", (password, id))
        con.commit()
        print("The record updated successfully")
    except Exception as e:
        print(e)


def delete_record(con, nickname):
    query = "DELETE FROM users WHERE nickname LIKE ?;"
    try:
        cur = con.cursor()
        cur.execute(query, (nickname,))
        con.commit()
        print("The record deleted successfully")
    except Exception as e:
        print(e)


""" def main():
    con = sql_connection()
    create_table(con)
    entities = ('Anna', '9009pass', 'little_ana')
    insert_data(con, entities)
    select_all(con)
    update_data(con, 'anna_12', 1)
    delete_record(con, 'alan_wake_000')
    con.close() """
