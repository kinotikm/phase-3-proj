import sqlite3
from colorama import Fore

class CarsDB:
    def _init_(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def validate_name(self, brand):
        if not isinstance(brand, str):
            print(Fore.RED + "Error: Brand must be a string.")
            return False
        if len(brand.strip()) == 0:
            print(Fore.RED + "Error: Brand cannot be empty.")
            return False
        return True

    def validate_year(self, year):
        try:
            year = int(year)
            if len(str(year)) == 4:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_price(self, price):
        try:
            float(price)
            return True
        except ValueError:
            return False

    def add_car(self, brand, year_of_make, price):
        if not self.validate_name(brand):
            print(Fore.RED + "Invalid brand name. Please enter a valid name.")
            return
        if not self.validate_year(year_of_make):
            print(Fore.RED + "Invalid year of make. Please enter a valid year.")
            return
        if not self.validate_price(price):
            print(Fore.RED + "Invalid price. Please enter a valid price.")
            return
        
        self.cursor.execute("INSERT INTO cars(brand, year_of_make, price) VALUES(?, ?, ?)",
                             (brand, year_of_make, price))
        self.conn.commit()

    def list_cars(self):
        self.cursor.execute("SELECT * FROM cars")
        return self.cursor.fetchall()