from Class_Shop_data_base import Shop_database
from Class_Shop_data_base import connect_table
import sqlite3

class Products:
    def __init__(self,name_product,quantity,price,category,db_name = "Shop_data_base.db"):
        self.name_product = name_product.capitalize()
        self.quantity = quantity
        self.price = price
        self.category = category
        self.db_name = db_name

    @connect_table
    def add_product(self):
        self.cursor.execute(f"INSERT INTO products (name_product,quantity,price,category) values (?,?,?,?)",(self.name_product, self.quantity, self.price,self.category))

    def __str__(self):
        return self.price,self.quantity,self.name_product


    def set_product(self,name,create_price,create_quantity):
        con = sqlite3.connect("Shop_data_base.db")
        cursor = con.cursor()
        cursor.execute('UPDATE products SET quantity = ?,price = ? WHERE name_product like ?', (create_quantity, create_price, name))
        con.commit()
        con.close()

    def del_product(self,name):
        name = name.capitalize()
        con = sqlite3.connect("Shop_data_base.db")
        cursor = con.cursor()
        cursor.execute("DELETE from products where name_product like ?", [name])
        con.commit()
        con.close()

    def show_products(self):
        con = sqlite3.connect("Shop_data_base.db")
        cursor = con.cursor()
        res = cursor.execute('select * from products')
        products = (con, res)
        for products in res:
            print(f"Название: {products[1]} Количество: {products[2]} Цена: {products[3]} Категория: {products[4]}")
        con.commit()
        con.close()
