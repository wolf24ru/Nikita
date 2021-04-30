def DocIsExist(directories):
    """ DocIsExist(directories)
    Function for input number of document
    directories: dictionary of document shelf's """

    while True:
        doc_number = input('\nВвидте номер документа:\n')

        if [doc_list
            for doc_list in directories.values()
                if doc_number in doc_list]:
            return doc_number
        else:
            print('Вы ввели не существующий документ')


def NameFormNumberDoc(documents, directories):
    """ NameFormNumberDoc(documents)
    Function requests document's number and return owners name
    documents: list of documents
    directories: dictionary of document shelf's """

    document_number = DocIsExist(directories)
    return [doc_element.get('name')
            for doc_element in documents
            if doc_element.get('number') == document_number][0]
    # return [doc_element.get('name') for doc_element in documents]


def ShelfFormNumberDoc(directories):
    """ ShelfFormNumberDoc(directories)
    Function requests document's number and return shelf's think
    directories: dictionary of document shelf's """

    document_number = DocIsExist(directories)
    return [shelf_number
            for shelf_number, doc_number in directories.items()
            if document_number in doc_number][0]


def AllDocumentList(documents):
    """ AllDocumentList(documents)
    Function return list of all documents
    documents: list of documents """

    return[list(doc_element.values()) for doc_element in documents]


def AddNewDocument(documents_dict, directories_dict):
    """ AddNewDocument(documents_dict, directories_dict)
    Function creating new documents and added in list
    documents_dict: list of documents
    directories_dict: dictionary of document shelf's """

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


def DeleteDocument(documents, directories):
    """ DeleteDocument(documents, directories)
    Function deleted document from all lists
    documents: list of documents
    directories: dictionary of document shelf's """

    document_number = DocIsExist(directories)

    for doc_element in documents:
        if document_number == doc_element.get('number'):
            documents.pop(documents.index(doc_element))
            break

    for shelf, value in directories.items():
        if document_number in value:
            directories.get(shelf).remove(document_number)
            break
    print(f'документ с номером {document_number} был удален')


def СhangeShelf(directories):
    """СhangeShelf(directories)
    Function change place of document in shelfs
    directories: dictionary of document shelf's
    """

    doc_number = DocIsExist(directories)

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


def AddShelf(directories):
    """ AddShelf(directories)
    to adding new shelfs
    directories: dictionary of document shelf's
    """
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

# ----------------------------------------------------------------------------
# Task 1
print('\nПоиск человека по номеру документа:')
people = NameFormNumberDoc(documents, directories)
print(people)

print('\nПоиск номера полки по номеру документа:')
shelf = ShelfFormNumberDoc(directories)
print(f'Номер полки: {shelf}')

print('\nВывод списка документов:\n')
forma_doc = AllDocumentList(documents)
print(forma_doc)

print('\nДобавление нового документа\n')
AddNewDocument(documents, directories)
print(documents, '\n', directories)

# ----------------------------------------------------------------------------
# Task 2
print('\nУдаление документа')
DeleteDocument(documents, directories)
print('\n', documents, '\n', directories)

print('\nДобавление полки\n')
AddShelf(directories)
print('\n', documents, '\n', directories)

print('\nПеремещение документа на другую полку')
СhangeShelf(directories)
print('\n', documents, '\n', directories)
