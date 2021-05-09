class Animal():
    """Animal"""
    all_animal = []

    def __init__(self, type_animal, name, weight):
        self.name = name
        self.type_animal = type_animal
        self.weight = weight
        Animal.all_animal.append(self)

    def Feed(self):
        print(f'{self.type_animal}, {self.name} было покормелнно')

    def SayName(self):
        print(f'Это {self.type_animal} - зовут {self.name}')


class Goat(Animal):

    def Milking(self):
        print(f'{self.type_animal}, {self.name} подоенна')

    def Voice(self):
        print(f'{self.type_animal} {self.name}, блеет')


class Cow(Animal):

    def Milking(self):
        print(f'{self.type_animal}, {self.name} подоенна')

    def Voice(self):
        print(f'{self.type_animal} {self.name}, мычит')


class Sheep(Animal):

    def Cut(self):
        print(f'{self.type_animal}, {self.name} пострижена')

    def Voice(self):
        print(f'{self.type_animal} {self.name}, блеет')


class Birds(Animal):
    def ColletEggs(self):
        print(f'Сбор яиц у {self.type_animal}, {self.name}')


class Goose(Birds):
    def Voice(self):
        print(f'{self.type_animal} {self.name}, гогочет')


class Сhicken(Birds):
    def Voice(self):
        print(f'{self.type_animal} {self.name}, кудахчет')


class Duck(Birds):
    def Voice(self):
        print(f'{self.type_animal} {self.name}, крякает')


goose_white = Goose('Гусь', 'Белый', 6)
goose_gray = Goose('Гусь', 'Серый', 7)

сow_1 = Cow('Корова', 'Манька', 760)

sheep_1 = Sheep('Обечка', 'Барашек', 50)
sheep_2 = Sheep('Обечка', 'Кудрявый', 54)

сhicken_1 = Сhicken('Курца', 'Ко-Ко', 1.5)
сhicken_2 = Сhicken('Курца', 'Кукареку', 1.9)

goat_1 = Goat('Коза', 'Рога', 38)
goat_2 = Goat('Коза', 'Копыта', 40)

duck_1 = Duck('Утка', 'Кряква', 4)

weight_all_animals = sum([i.weight for i in Animal.all_animal])
heaviest_animal = max([i.weight, i.name, i.type_animal]
                      for i in Animal.all_animal)

print(f'Общая ссума всех животных: {weight_all_animals} кг')
print(    f'Самое тяжолое животное - {heaviest_animal[2]} {heaviest_animal[1]}, его вес {heaviest_animal[0]}')
