# Поменять названия переменным, функциям

def People(document_number, documents):
    return [x['name']
            if x['number'] == document_number else 'Такого номер нет'
            for x in documents][0]


def Shelf(document_number, directories):
    return[x
           if document_number in i else 'Такого номер нет'
           for x, i in directories.items()][0]


def DocumentList(documents):
    return[list(x.values()) for x in documents]


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []}


# n = People(input('введите номер документа?'), documents)

# p = Shelf('2207', directories)

# s = DocumentList(documents)

# add – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
