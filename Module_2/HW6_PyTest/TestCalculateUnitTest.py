# import hw5
from hw5 import documents, directories
from hw5 import doc_is_exist, name_form_number_doc, shelf_form_number_doc, all_document_list, add_new_document, \
    delete_document, change_shelf, add_shelf


class TestCalculatePytest:
    def test_doc_is_exist(self):
        assert doc_is_exist(directories) == 1

    def test_find_person_on_number(self):
        assert name_form_number_doc(documents, directories) == 6
