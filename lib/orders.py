import sqlite3
import datetime
from colorama import Fore

class OrdersDB:
    def _init_(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def validate_quantity(self, quantity):
        try:
            int(quantity)
            return True
        except ValueError:
            return False

    def validate_price(self, price):
        try:
            float(price)
            return True
        except ValueError:
            return False

    def add_order(self, client_id, order_date, quantity, total_price):
        try:
            datetime.datetime.strptime(order_date, "%Y-%m-%d")
        except ValueError:
            print(Fore.RED + "Invalid date format. Please enter a valid date.")
            return

        if not self.validate_quantity(quantity):
            print(Fore.RED + "Invalid quantity. Please enter a valid quantity.")
            return
        if not self.validate_price(total_price):
            print(Fore.RED + "Invalid total price. Please enter a valid price.")
            return
        
        self.cursor.execute("INSERT INTO orders(client_id, order_date, quantity, total_price) VALUES(?, ?, ?, ?)",
                             (client_id, order_date, quantity, total_price))
        self.conn.commit()

    def search_client_by_id(self, client_id):
        self.cursor.execute("SELECT * FROM orders WHERE client_id=?", (client_id,))
        orders = self.cursor.fetchall()
        return orders

    def list_orders(self):
        self.cursor.execute('''
            SELECT orders.order_id, orders.order_date, clients.name, orders.quantity, orders.total_price
            FROM orders
            JOIN clients ON orders.client_id = clients.id
        ''')
        return self.cursor.fetchall()