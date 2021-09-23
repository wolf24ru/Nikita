def doc_is_exist(directories):
    """ doc_is_exist(directories)
    Function for input number of document
    directories: dictionary of document shelf's """

    while True:
        doc_number = input('\nВведите номер документа:\n')

        if [doc_list
            for doc_list in directories.values()
                if doc_number in doc_list]:
            return doc_number
        else:
            print('Вы ввели не существующий документ')
            return -1


def name_form_number_doc(documents, directories):
    """ name_form_number_docdoc_is_exist(documents)
    Function requests document's number and return owners name
    documents: list of documents
    directories: dictionary of document shelf's """

    print('\nПоиск человека по номеру документа:')
    document_number = doc_is_exist(directories)
    for document in documents:
        if document.get('number') == document_number:
            return document.get('name')


def shelf_form_number_doc(directories):
    """ shelf_form_number_doc(directories)
    Function requests document's number and return shelf's think
    directories: dictionary of document shelf's """

    print('\nПоиск номера полки по номеру документа:')
    document_number = doc_is_exist(directories)
    return [shelf_number
            for shelf_number, doc_number in directories.items()
            if document_number in doc_number][0]


def all_document_list(documents):
    """ all_document_list(documents)
    Function return list of all documents
    documents: list of documents """

    print('Вывод списка документов')
    for document in documents:
        print(list(document.values()))
    # print([list(doc_element.values()) for doc_element in documents])


def add_new_document(documents_dict, directories_dict):
    """ add_new_document(documents_dict, directories_dict)
    Function creating new documents and added in list
    documents_dict: list of documents
    directories_dict: dictionary of document shelf's """

    print('\nДобавление нового документа\n')
    doc_type = input('Введите тип документа:\n')
    doc_number = input('Ввидте номер документа\n')
    doc_name = input('Введите имя\n')
    while True:
        doc_shel = input('Введите номер полки\n')
        if doc_shel in [shelf_number
                        for shelf_number in directories_dict.keys()]:
            break
        else:
            print('Вы ввели номер не существующей полки, попробуйте снова\n')

    documents_dict.append({"type": doc_type,
                           "number": doc_number,
                           "name": doc_name})
    directories_dict.get(doc_shel).append(doc_number)
    print('Новый документ добавлен')


def delete_document(documents, directories):
    """ delete_document(documents, directories)
    Function deleted document from all lists
    documents: list of documents
    directories: dictionary of document shelf's """
    print('\nУдаление документа')

    document_number = doc_is_exist(directories)

    for doc_element in documents:
        if document_number == doc_element.get('number'):
            documents.pop(documents.index(doc_element))
            break

    for shelf, value in directories.items():
        if document_number in value:
            directories.get(shelf).remove(document_number)
            break
    print(f'документ с номером {document_number} был удален')


def change_shelf(directories):
    """change_shelf(directories)
    Function change place of document in shelfs
    directories: dictionary of document shelf's
    """

    print('Перемещение документа на другую полку\n')
    doc_number = doc_is_exist(directories)

    while True:
        doc_shelf = input(
            'Введите номер полки на которую необходимо переместить документ\n')
        if doc_shelf in [shelf_number
                         for shelf_number in directories.keys()]:
            break
        else:
            print('Вы ввели номер не существующей полки, попробуйте снова\n')

    for shelf, value in directories.items():
        if doc_number in value:
            directories.get(shelf).remove(doc_number)
            break

    directories.get(doc_shelf).append(doc_number)
    print(
        f'Документ с номером {doc_number} был перемещен на полку {doc_shelf}')


def add_shelf(directories):
    """ add_shelf(directories)
    to adding new shelfs
    directories: dictionary of document shelf's
    """

    print('Добавление новой полки\n')
    while True:
        new_shelf = input(
            'Введите номер полки которую необходимо добавить\n')
        if new_shelf not in [shelf_number
                             for shelf_number in directories.keys()]:
            directories.update({new_shelf: []})
            print(f'Полка {new_shelf} была добавлена')
            break
        else:
            print('Вы ввели номер существующей полки, попробуйте снова\n')


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []}

if __name__ == '__main__':
    while True:
        print('''
    1: Поиск человека по номеру документа
    2: Поиск номера полки по номеру документа
    3: Вывод списка документов
    4: Добавление нового документа
    5: Удаление документа
    6: Добавление новой полки
    7: Перемещение документа на другую полку
    8: Вывод словаря документов
    9: Вывод словаря полок
    0: Выход\n
    ''')

        try:
            choice = int(input('Введите номер необходимого действия: \n>> '))
        except ValueError:
            choice = 10

        if choice == 1:
            people = name_form_number_doc(documents, directories)
            print(people)
        elif choice == 2:
            shelf = shelf_form_number_doc(directories)
            print(f'Номер полки: {shelf}')
        elif choice == 3:
            all_document_list(documents)
        elif choice == 4:
            add_new_document(documents, directories)
        elif choice == 5:
            delete_document(documents, directories)
        elif choice == 6:
            add_shelf(directories)
        elif choice == 7:
            change_shelf(directories)
        elif choice == 8:
            print('Словарь документов:')
            for document in documents:
                print(document)
        elif choice == 9:
            print('Словарь полок:')
            for num_shelf, num_doc in directories.items():
                print(f'{num_shelf}: {num_doc}')
        elif choice == 0:
            exit()
        else:
            print('Вы ввели несуществующую команду. Попробуйте снова')
