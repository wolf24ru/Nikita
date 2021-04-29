def DocIsExist(directories):
    while True:
        doc_number = input('Ввидте номер документа:\n')

        if [doc_list
            for doc_list in directories.values()
                if doc_number in doc_list]:
            return doc_number
        else:
            print('Вы ввели не существующий документ')


def NameFormNumberDoc(documents):
    document_number = input('Введите номер документа?')
    return [doc_element['name']
            if doc_element['number'] == document_number else 'Такого номер нет'
            for doc_element in documents][0]


def ShelfFormNumberDoc(directories):
    document_number = input('Введите номер документа?')
    return[shelf_number
           if document_number in doc_number else 'Такого номер нет'
           for shelf_number, doc_number in directories.items()][0]


def AllDocumentList(documents):
    return[list(doc_element.values()) for doc_element in documents]


def AddNewDocument(documents_dict, directories_dict):
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
    document_number = DocIsExist(directories)

    for doc_element in documents:
        if document_number == doc_element.get('number'):
            documents.pop(documents.index(doc_element))
            break

    for shelf, value in directories.items():
        if document_number in value:
            directories.get(shelf).remove(document_number)
            break


# проверить работоспасбоность
def СhangeShelf(directories):
    doc_number = DocIsExist(directories)

    while True:
        doc_shelf = input(
            'Введите номер полки на которую необходимо переместить документ\n')
        if doc_shelf in [shelf_number
                         for shelf_number in directories.keys()]:
            break
        else:
            print('Вы ввели номер не существующей полки, попробуйте снова\n')


def AddShelf():
    pass


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []}


# p = NameFormNumberDoc(documents)
# s = ShelfFormNumberDoc(directories)
# l = AllDocumentList(documents)
# AddNewDocument(documents, directories)
DeleteDocument(documents, directories)
print(documents, '\n')
print(directories)
# СhangeShelf(directories)
