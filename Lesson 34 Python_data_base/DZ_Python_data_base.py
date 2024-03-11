import sqlite3 as sq

def decor(func):
    def wrapper(*args,**kwargs):
        with sq.connect("Clients.db") as con:
            con.cursor()
            func(*args,**kwargs)
    return wrapper

with sq.connect("Clients.db") as con:
    con.cursor()
    con.execute("""CREATE TABLE IF NOT EXISTS clients (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    name_client TEXT NOT NULL,
    surname TEXT NOT NULL,
    address TEXT NOT NULL,
    number_phone TEXT NOT NULL
)""")
@decor
def add_information(name,surname,address,number):
    con.execute(f"INSERT INTO clients (name_client,surname,address,number_phone) values(?,?,?,?)",(name,surname,address,number))
    con.commit()
    con.close()
@decor
def show_info():
    results = con.execute("SELECT * FROM clients")
    for result in results:
        print(result)

while True:
    print("Работа с СУБД SQLite")
    command_base = input("""
1.Ввод данных
2.Просмотр данных
3.Выход
""")
    match command_base:
        case "1":
            n = input("Введите имя клиента: ")
            s_n = input("Введите Фамилию клиента: ")
            ad = input("Введите адрес клиента: ")
            number = input("Введите номер телефона клиента: ")
            add_information(n,s_n,ad,number)
        case "2":
            show_info()
        case "3":
            break
