import sqlite3
from Class_Shop_data_base import connect_table
from Class_Shop_data_base import Shop_database
from Class_Products import Products


class Users:
    basket = {}
    def __init__(self,name,phone,address):
        self.name = str(name.capitalize())
        self.phone = str(phone.capitalize())
        self.address = str(address.capitalize())
        self.db_name = "Shop_data_base.db"

    @classmethod
    def del_basket(cls):
        del cls.basket["basket_1"]

    @connect_table
    def add_user(self):
        self.con.execute(f"INSERT INTO users (name_user,phone_number,address) values (?,?,?)",(self.name, self.phone, self.address))

    def set_user(self,name, create_phone, create_address):
        con = sqlite3.connect("Shop_data_base.db")
        cursor = con.cursor()
        cursor.execute(f"UPDATE users SET phone_number = ?,address = ? where name_user like ?", (create_phone, create_address, name))
        con.commit()
        con.close()

    def add_product_in_basket(self,name_product,quantity):
        self.basket["basket_1"] = name_product, quantity
        print(self.basket)
        # con = sqlite3.connect("Shop_data_base.db")
        # cursor = con.cursor()
        # res = cursor.execute('select * from products')
        # products = (con, res)
        # for products in res:
        #     print(f"Название: {products[1]} Количество: {products[2]} Цена: {products[3]} Категория: {products[4]}")
        #
        # self.basket["basket_1"] = name_product,quantity
        # print(self.basket)
        # print(type(self.basket))
        # pick_result = cursor.execute("select * from products where name_prodict like ?",name_product)
        # if pick_result.fetchone() is True:
        #     print(type(pick_result.fetchone()))
        #     print(pick_result.fetchone())
        # con.commit()
        # con.close()






