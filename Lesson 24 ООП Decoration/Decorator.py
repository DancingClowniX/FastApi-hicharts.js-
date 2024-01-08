
class Cat:
    def __init__(self,nickname:str):

        self.__nickname = self.validate_nickname(nickname)
        self.__mood = 100
        self.__energy = 100

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self,nickname):
        self.validate_nickname(nickname)
        self.__nickname = nickname
    @property #обращается как к атрибуту класса
    def mood(self):
        return self.__mood
    @mood.setter# обращается по примеру cat.mood = value
    def mood(self,mood):
        self.__mood = mood

    @staticmethod #декораторы добавляют новый функционал
    def validate_nickname(nickname):
        if type(nickname)!= str:
            raise "nickname must be str"
        if len(nickname)<5:
            raise "nickname must be 5 or more symbols"
        if nickname.isspace():
            raise "must not be only space symbols"
        return nickname

cat1 = Cat("Clarissa Starling")
print(cat1.get_nickname())
#cat1.set_nickname("v")
#print(cat1.get_nickname())
try:
    Cat.validate_nickname("v")
    print("validate")
except:
    print("non validate")

print(cat1.mood)
cat1.mood = 150# вместо cat.set_mood()
print(cat1.mood)