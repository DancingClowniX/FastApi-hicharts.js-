class SantaClaus:
    def __init__(self,name,age,quantity_gift):
        self.name = name
        self.age = age
        self.quantity_gift = quantity_gift
    def give_gifts(self):
        if 0<self.age<18:
            if self.quantity_gift % 10==1 and self.quantity_gift !=11:
                print(f"Дед мороз даёт ребёнку {self.name} {self.quantity_gift} подарок!")
            elif 1<self.quantity_gift<5 or 1<self.quantity_gift % 10<5:
                print(f"Дед мороз даёт ребёнку {self.name} {self.quantity_gift} подарка!")
            else:
                print(f"Дед мороз даёт ребёнку {self.name} {self.quantity_gift} подарков!")
        elif self.age==0:
            print(f'{self.name} младенец, пёлёнки нужны, а не подарки')
        else:
            print(f'{self.name}, это взрослый человек, Дед мороз не даёт подарки взрослым людям')
    def update_age(self):
        self.age += 1
        print(f"{self.name} растёт, возраст составляет {self.age}!")
kid1 = SantaClaus("David",18,4)
kid1.give_gifts()
kid1.update_age()
kid2 = SantaClaus("Rebecca",0,21)
kid2.give_gifts()
kid2.update_age()