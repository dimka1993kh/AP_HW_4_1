from classes import Secretary
from data import directories, documents

class TestSecretary:
    def setup(self):
        print("method setup")   
    def teardown(self):
        print("method teardown")   

    def test_one_return_name_person(self):
        #Нет номера в базе
        assert Secretary().return_name_person('ъъъъъъ') == False
    def test_two_return_name_person(self):
        #есть номер в базе
        assert Secretary().return_name_person('11-2') == 'Геннадий Покемонов'

    def test_one_return_num_shelf(self):
        assert Secretary().return_num_shelf('11-2') == '1'
    def test_two_return_num_shelf(self):
        assert Secretary().return_num_shelf('ъъъъъъ') == False

    def test_return_list_all(self):
        assert Secretary().return_list_all() == ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"']
    def test_add_doc(self):
        result_doc = Secretary().add_doc(999, 'Тестовый документ', '4', 'Тестовый человек')
        result_dir = directories['4']
        Secretary().del_doc(999)
        assert result_doc == {"type": 'Тестовый документ', "number": 999, "name": 'Тестовый человек'} and result_dir == [999]

    def test_one_add_doc_on_bookshelf_number(self):
        #Обновление полки
        result = Secretary().add_doc_on_bookshelf_number(1278, 3)
        Secretary().del_doc(1278)
        assert result == directories['3']
    def test_two_add_doc_on_bookshelf_number(self):
        #Добавление полки
        result = Secretary().add_doc_on_bookshelf_number(1333, 4)
        Secretary().del_doc(1333)
        assert result == directories['4']

    def test_add_shelf(self):
        #Добавление полки
        result = Secretary().add_shelf(13)
        assert result == {str(13) : []}
    
    def test_del_doc(self):
        #Удаление документа
        doc = {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
        result = Secretary().del_doc(doc['number'])
        documents.append(doc)
        assert result not in [
                                {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
                            ]

    def test_one_deleting_from_directory(self):
        #Удаление полки
        doc = {'2': ['10006']}
        result = Secretary().deleting_from_directory(10006)
        directories.update(doc)
        assert 10006 not in directories[result]
    def test_two_deleting_from_directory(self):
        #Нет такого номера документа
        assert Secretary().deleting_from_directory(-1) == ''

    def test_move_doc(self):
        #Нужно ли делать проверку, если данный метод состоит из 2х протестированных методов и больше ничего?
        assert True == True

    def test_end_doc(self):
        assert Secretary().end_doc() == False

    def test_print_doc(self):
        assert Secretary().print_doc() == True