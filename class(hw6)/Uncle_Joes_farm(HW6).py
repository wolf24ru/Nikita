class Animal():
    """Animal"""
    all_animal = []

    def __init__(self, name, weight):
        '''иницилизация класса (имя животного, вес животного)
        '''
        self.name = name
        self.weight = weight

        Animal.all_animal.append(self)

    def Feed(self):
        print(f'{self.type_animal}, {self.name} было покормелнно')

    def SayName(self):
        print(f'Это {self.type_animal} - зовут {self.name}')


class Goat(Animal):
    type_animal = 'Коза'

    def Milking(self):
        print(f'{self.type_animal}, {self.name} подоенна')

    def Voice(self):
        print(f'{self.type_animal} {self.name}, блеет')


class Cow(Animal):
    type_animal = 'Корова'

    def Milking(self):
        print(f'{self.type_animal}, {self.name} подоенна')

    def Voice(self):
        print(f'{self.type_animal} {self.name}, мычит')


class Sheep(Animal):
    type_animal = 'Овечка'

    def Cut(self):
        print(f'{self.type_animal}, {self.name} пострижена')

    def Voice(self):
        print(f'{self.type_animal} {self.name}, блеет')


class Birds(Animal):
    def ColletEggs(self):
        print(f'Сбор яиц у {self.type_animal}, {self.name}')


class Goose(Birds):
    type_animal = 'Гусь'

    def Voice(self):
        print(f'{self.type_animal} {self.name}, гогочет')


class Сhicken(Birds):
    type_animal = 'Курца'

    def Voice(self):
        print(f'{self.type_animal} {self.name}, кудахчет')


class Duck(Birds):
    type_animal = 'Утка'

    def Voice(self):
        print(f'{self.type_animal} {self.name}, крякает')


goose_white = Goose('Белый', 6)
goose_gray = Goose('Серый', 7)

сow_1 = Cow('Манька', 760)

sheep_1 = Sheep('Барашек', 50)
sheep_2 = Sheep('Кудрявый', 54)

сhicken_1 = Сhicken('Ко-Ко', 1.5)
сhicken_2 = Сhicken('Кукареку', 1.9)

goat_1 = Goat('Рога', 38)
goat_2 = Goat('Копыта', 40)

duck_1 = Duck('Кряква', 4)

# Задача №2
[p.Feed() for p in Animal.all_animal]
goose_gray.ColletEggs()
сow_1.Milking()
sheep_1.Cut()
сhicken_1.ColletEggs()
goat_1.Milking()
duck_1.ColletEggs()

# Звдание №3
weight_all_animals = sum([i.weight for i in Animal.all_animal])
heaviest_animal = max([i.weight, i.name, i.type_animal]
                      for i in Animal.all_animal)
print('\n\n\n')
print(f'Общая ссума всех животных: {weight_all_animals} кг\n')
print(f'Самое тяжолое животное - {heaviest_animal[2]} {heaviest_animal[1]}, его вес {heaviest_animal[0]} кг')
