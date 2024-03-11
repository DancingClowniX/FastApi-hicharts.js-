# Задача 3: Работа с файлами
# Реализуйте класс FileManager, представляющий управление файлами.
# Класс должен содержать методы read_file и write_file,
# которые будут читать данные из файла и записывать данные в файл соответственно.
# Создайте собственный класс исключения FileNotFoundError,
# который будет возбуждаться, если файл не может быть найден при чтении или записи.
#

class AtributeError(Exception):
    def __str__(self):
        return f"atibute name is not str"

class FileNotFoundError(Exception):
    def __str__(self):
        return "File not found and not must be read"

class FileManager:
    def __init__(self, name: str):
        if type(name) !=str:
            raise AtributeError
        else:
            self.name = name

    def read_file(self):
        with open(f"{self.name}.txt", encoding = "utf-8") as f:
            f.read()

    def write_file(self):
        with open(f"{self.name}.txt", "x") as f:
            f.write()
#
# try:
#     new_file = FileManager(9) # атрибут не str
# except AtributeError:
#     print(AtributeError())

#
# try:
#     new_file = FileManager("text") # атрибут существует но файла нет режим чтения
#     new_file.read_file()
#
# except:
#     print(FileNotFoundError())

#
# try:
#       new_file = FileManager("text") # атрибут существует но файла нет режим записи
#       new_file.write_file()
# except :
#     print(FileNotFoundError())
