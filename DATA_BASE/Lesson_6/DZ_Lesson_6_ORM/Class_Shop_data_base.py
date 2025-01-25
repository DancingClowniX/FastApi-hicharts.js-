import sqlite3

def connect_table(func):
    def wrapper(self,*args,**kwargs):
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()
        result = func(self,*args,**kwargs)
        self.con.commit()
        self.con.close()
        return result
    return wrapper

class Shop_database:
    def __init__(self,db_name = "Shop_data_base.db"):
        self.db_name = db_name
        self.create_table_orders()
        self.create_table_users()
        self.create_table_products()
        self.user_list = []

    @connect_table
    def create_table_orders(self):
        self.con.execute("""CREATE TABLE IF NOT EXISTS orders (
            id_order INTEGER PRIMARY KEY,
            name_order TEXT NOT NULL,
            status_order TEXT NOT NULL,
            id_user_order INTEGER REFERENCES users (id_user)
        )""")

    @connect_table
    def create_table_users(self):
        self.con.execute("""CREATE TABLE IF NOT EXISTS users (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            name_user TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            address TEXT NOT NULL
        )""")

    @connect_table
    def create_table_products(self):
        self.con.execute("""CREATE TABLE IF NOT EXISTS products (
            id_product INTEGER PRIMARY KEY AUTOINCREMENT,
            name_product TEXT NOT NULL,
            quantity INTEGER,
            price INTEGER,
            category TEXT NOT NULL
            )""")

    @connect_table
    def validation(self,name):
        name = name.capitalize()
        res = self.con.execute("SELECT name_user from users where name_user = ?", [name])
        if res.fetchone() is None:
            return False
        else:
            return True

    @connect_table
    def validation_prod(self, name):
        name = name.capitalize()
        res = self.con.execute("SELECT name_product from products where name_product = ?", [name])
        if res.fetchone() is None:
            return False
        else:
            return True
