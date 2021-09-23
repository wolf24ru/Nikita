<<<<<<< HEAD
import pytest
from hw5 import documents, directories
from hw5 import doc_is_exist, name_form_number_doc, shelf_form_number_doc, all_document_list, add_new_document, \
	delete_document, change_shelf, add_shelf


class TestCalculatePytest:

	def setup(self):
		pass

	@pytest.mark.parametrize('num_doc', [
		'2207 876234',
		'11-2',
		'10006',
		' ',
		'r4dd',
		433,
		'433'
	])
	def test_doc_is_exist_int(self, monkeypatch, num_doc):
		monkeypatch.setattr('builtins.input', lambda _: num_doc)
		assert doc_is_exist(directories) == num_doc


	# def test_find_person_on_number(self):
	# assert name_form_number_doc(documents, directories) == 6
=======
# import hw5
import pytest

from hw5 import documents, directories
from hw5 import doc_is_exist, name_form_number_doc, shelf_form_number_doc, add_new_document, \
    delete_document, change_shelf, add_shelf


class TestCalculatePytest:
    test_documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "abra-codabra", "number": "0000", "name": "Павлуша Шмелев"},
        {"type": 54, "number": 10006, "name": 543},
        {"type": 54, "number": 10006, "name": "Аристарх Павлов"},
        {"type": "", "number": "", "name": ""},
        {"type": None, "number": None, "name": None},
        {"type": False, "number": False, "name": False},
    ]

    # Проверка ввода данных
    @pytest.mark.parametrize('input_enter', [i.get('number') for i in test_documents])
    def test_doc_is_exist(self, monkeypatch, input_enter):
        monkeypatch.setattr('builtins.input', lambda _: input_enter)
        assert doc_is_exist(directories) == input_enter

    # Поиск человека по номеру документа
    @pytest.mark.parametrize("input_enter, user_name", [[i.get('number'), i.get('name')] for i in test_documents])
    def test_find_person_on_number(self, monkeypatch, input_enter, user_name):
        monkeypatch.setattr('builtins.input', lambda _: input_enter)
        assert name_form_number_doc(documents, directories) == user_name

    # Поиск номера полки по номеру документа
    @pytest.mark.parametrize("input_enter", [i.get('number') for i in test_documents])
    def test_shelf_number(self, monkeypatch, input_enter):
        monkeypatch.setattr('builtins.input', lambda _: input_enter)
        assert shelf_form_number_doc(directories) in ['1', '2', '3']

    # Добавление нового документа
    @pytest.mark.parametrize("input_type, input_number, input_name, input_shel", [
        ['', '', '', ''],
        ['mein_passport', '999-23-56', 'Василий Пупкин', '3'],
        [125, '5526', 'Матфиенко Павел', '2'],
        ['doc_1', 5534, 'Матфиенко Павел', '2'],
        ['doc_1', '5578-3', 324, '3'],
        ['doc_1', '5578-3', 'Матфиенко Павел', '5'],
        ['doc_1', '5578-3', 'Матфиенко Павел', 5],
        ['doc_1', '5578-3', 'Матфиенко Павел', 2],
        [None, None, None, '2'],
        [False, False, False, '2'],
    ])
    def test_add_document(self, monkeypatch, input_type, input_number, input_name, input_shel):
        responses = iter([input_type, input_number, input_name, input_shel])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert add_new_document(documents, directories) == 1
        for document in documents:
            print(document)

    # Добавление новой полки
    @pytest.mark.parametrize("input_shel", ['1', 2, 'adf', '', '4', None, False])
    def test_add_shelf(self, monkeypatch, input_shel):
        monkeypatch.setattr('builtins.input', lambda _: input_shel)
        assert add_shelf(directories) == 1

    # Перемещение документа на другую полку
    @pytest.mark.parametrize("input_number, input_shel_new", [
        ['10006', '3'],
        ['10006', '10'],
        ['10006', 3],
        [10006, '3'],
        ['2345', '3'],
        [None, None],
        [False, False],
    ])
    def test_change_shelf(self, monkeypatch, input_number, input_shel_new):
        responses = iter([input_number, input_shel_new])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert change_shelf(directories) == 1

# Удаление документа
    @pytest.mark.parametrize("input_number", [i.get('number') for i in test_documents])
    def test_delete_document(self, monkeypatch, input_number):
        monkeypatch.setattr('builtins.input', lambda _: input_number)
        assert delete_document(documents, directories) == 1

if __name__ == '__main__':
    pytest.main()
>>>>>>> 314402679414cae4a55aa6413d0e6d223ea8b450
