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
