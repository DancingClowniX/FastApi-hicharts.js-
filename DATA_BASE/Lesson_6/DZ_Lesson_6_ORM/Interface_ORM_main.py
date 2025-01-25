import sqlite3
from Class_Shop_data_base import connect_table
from Class_Shop_data_base import Shop_database
from Class_Products import Products
from Class_users import Users
from Class_Products import Products
import smtplib
def line():
    print("*************************************************")

while True:
    data_base_shop = Shop_database()
    print("Система управления заказами магазина Shop.ru")
    command_line = input("""Войдите в учётную запись:
1.Войти как пользователь
2.Войти как администратор
3.Выход
""")
    match command_line:
        case "1":
            line()
            command_user = input("""Зарегистируйтесь или войдите в систему:
1.Зарегистироваться
2.Войти в систему
3.Выход
""")
            match command_user:
                case "1":
                    new_user_name = input("Введите имя: ")
                    new_user_phone = input("Введите телефон: ")
                    new_user_address = input("Введите адрес: ")
                    valid_new_user = data_base_shop.validation(new_user_name)
                    if valid_new_user == False:
                        new_user = Users(new_user_name,new_user_phone,new_user_address)
                        new_user.add_user()
                        data_base_shop.user_list.append(new_user)
                    else:
                        print("Вы уже зарегистрированы")
                        line()
                case "2":
                    user_name = input("Введите имя: ")
                    valid_user = data_base_shop.validation(user_name)
                    if valid_user == False:
                        break
                    else:
                        while True:
                            command_user_system = input("""
1.Посмотреть каталог
2.Выбрать товар
3.Посмотреть корзину и оформить заказ
4.Изменить данные
5.Назад
""")
                            match command_user_system:
                                case "1":
                                    Products.show_products(Products)
                                case "2":
                                    Products.show_products(Products)
                                    pick_name_product = input("Напишите название продукта: ")
                                    pick_quantity_product = input("Напишите количество: ")
                                    Users.add_product_in_basket(Users,pick_name_product,pick_quantity_product)
                                case "3":
                                    command_user_basket = input("""
1.Очистить корзину
2.Оформить заказ
3.Назад
""")
                                    match command_user_basket:
                                        case 1:
                                            Users.del_basket()
                                        case 2:
                                            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                                case "4":
                                    create_user_phone = input("Введите новый номер телефона: ")
                                    create_user_address = input("Введите новый адрес: ")
                                    set_data_user = Users.set_user(Users,user_name, create_user_phone, create_user_address)
                                case "5":
                                    break
                case _: break
        case "2":
            line()
            print("Введите данные чтобы зайти в систему: ")
            line()
            login = str(input("Введите логин: "))
            password = str(input("Введите пароль: "))
            match login,password:
                case "admin", "qwer1234":
                    line()
                    print("вы вошли в систему")
                    line()
                    while True:
                        command_admin = input("""
1.Добавить новый товар
2.Удалить товар из БД
3.Выполнить корректировку номенклатуры
4.Показать данные о товарах
5.Назад
""")
                        match command_admin:
                            case "1":
                                line()
                                name_prod = input("Введите название товара: ")
                                quantity_prod = input("Введите количество: ")
                                price_prod = input("Введите цену товара: ")
                                category_prod = input("Введите категорию товара: ")
                                validation_new_prod = data_base_shop.validation_prod(name_prod)
                                match validation_new_prod:
                                    case True:
                                        print("Данный товар уже есть")
                                    case False:
                                        new_product = Products(name_prod, quantity_prod, price_prod, category_prod)
                                        new_product.add_product()
                                        continue
                                continue
                            case "2":
                                line()
                                del_name_prod = input("Введите название удаляемого товара: ")
                                validation_del_prod = data_base_shop.validation_prod(del_name_prod)
                                match validation_del_prod:
                                    case True:
                                        line()
                                        Products.del_product(Products,del_name_prod)
                                        print(f"Товар {del_name_prod} удалён из базы")
                                        continue
                                    case False:
                                        line()
                                        print("Данного товара нет в базе данных")
                                        continue
                            case "3":
                                line()
                                set_name_prod = input("Введите название корректируемого товара: ")
                                validation_set_prod = data_base_shop.validation_prod(set_name_prod)
                                match validation_set_prod:
                                    case True:
                                        line()
                                        create_price_prod = input("Введите новую цену продукта: ")
                                        create_quantity_prod = input("Введите новое кол-во продукта: ")
                                        Products.set_product(Products,set_name_prod,create_price_prod,create_quantity_prod)
                                        print(f"Товар {set_name_prod} откорректирован")
                                    case False:
                                        line()
                                        print("Данного товара нет в базе данных")
                            case "4":
                                line()
                                Products.show_products(Products)
                            case _:
                                break
                case _:
                    break
        case _: break