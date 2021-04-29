def DocIsExist(directories):
    """ DocIsExist(directories)
    Function for input number of document
    directories: dictionary of document shelf's """

    while True:
        doc_number = input('Ввидте номер документа:\n')

        if [doc_list
            for doc_list in directories.values()
                if doc_number in doc_list]:
            return doc_number
        else:
            print('Вы ввели не существующий документ')


def NameFormNumberDoc(documents):
    """ NameFormNumberDoc(documents)
    Function requests document's number and return owners name
    documents: list of documents """

    document_number = input('Введите номер документа?')
    return [doc_element['name']
            if doc_element['number'] == document_number else 'Такого номер нет'
            for doc_element in documents][0]


def ShelfFormNumberDoc(directories):
    """ ShelfFormNumberDoc(directories)
    Function requests document's number and return shelf's think
    directories: dictionary of document shelf's """

    document_number = input('Введите номер документа?')
    return[shelf_number
           if document_number in doc_number else 'Такого номер нет'
           for shelf_number, doc_number in directories.items()][0]


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
people = NameFormNumberDoc(documents)
print(people)

shelf = ShelfFormNumberDoc(directories)
print(shelf)

forma_doc = AllDocumentList(documents)
print(forma_doc)

AddNewDocument(documents, directories)
print(documents, '\n', directories)
# ----------------------------------------------------------------------------
# Task 2
DeleteDocument(documents, directories)
print(documents, '\n', directories)

AddShelf(directories)
print(documents, '\n', directories)

СhangeShelf(directories)
print(documents, '\n', directories)
