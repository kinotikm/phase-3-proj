import sqlite3
from colorama import Fore

class ClientsDB:
    def _init_(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def validate_name(self, name):
        if not isinstance(name, str):
            print(Fore.RED + "Error: Name must be a string.")
            return False
        if len(name.strip()) == 0:
            print(Fore.RED + "Error: Name cannot be empty.")
            return False
        if name.isdigit():
            print(Fore.RED + "Error: Name cannot be numeric.")
            return False
        return True

    def validate_phone(self, phone_number):
        if not isinstance(phone_number, str):
            print(Fore.RED + "Error: Phone number must be a string.")
            return False
        if len(phone_number.strip()) == 0:
            print(Fore.RED + "Error: Phone number cannot be empty.")
            return False
        if not phone_number.isdigit() or len(phone_number) != 10:
            print(Fore.RED + "Error: Phone number must contain exactly 10 digits.")
            return False
        return True

    def validate_email(self, email):
        if "@" not in email or "." not in email:
            print(Fore.RED + "Error: Invalid email format.")
            return False
        return True

    def add_client(self, name, phone_number, email):
        if not self.validate_name(name):
            print(Fore.RED + "Invalid name. Please enter a valid name.")
            return
        if not self.validate_phone(phone_number):
            print(Fore.RED + "Invalid phone number. Please enter a valid phone number.")
            return
        if not self.validate_email(email):
            print(Fore.RED + "Invalid email. Please enter a valid email.")
            return
        
        self.cursor.execute("INSERT INTO clients(name, phone_number, email) VALUES(?, ?, ?)",
                             (name, phone_number, email))
        self.conn.commit()

    def search_client_by_name(self, name):
        self.cursor.execute("SELECT * FROM clients WHERE name=?", (name,))
        return self.cursor.fetchall()

    def search_client_by_id(self, client_id):
        self.cursor.execute("SELECT * FROM clients WHERE id=?", (client_id,))
        client = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM orders WHERE client_id=?", (client_id,))
        orders = self.cursor.fetchall()
        return client, orders

    def list_clients(self):
        self.cursor.execute("SELECT * FROM clients")
        return self.cursor.fetchall()

    def delete_client(self, client_id):
        self.cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
        self.cursor.execute("DELETE FROM orders WHERE client_id=?", (client_id,))
        self.conn.commit()