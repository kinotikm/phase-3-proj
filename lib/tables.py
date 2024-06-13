import sqlite3

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone_number TEXT NOT NULL,
                   email TEXT NOT NULL)
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
                   brand TEXT PRIMARY KEY,
                   year_of_make INTEGER NOT NULL,
                   price REAL NOT NULL)
                   ''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
                   order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   order_date DATE NOT NULL,
                   client_id INTEGER NOT NULL,
                   quantity INTEGER NOT NULL,
                   total_price REAL NOT NULL,
                   FOREIGN KEY (client_id) REFERENCES clients(id))
                   ''')
    
    conn.commit()

def get_connection():
    return sqlite3.connect("cars.db")