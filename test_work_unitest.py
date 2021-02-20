import unittest
from classes import Secretary
from data import directories, documents

class TestWork(unittest.TestCase):
    def setUp(self):
        print("method setUp")   
    def tearDown(self):
        print("method tearDown")   
    def test_one_return_name_person(self):
        #Нет номера в базе
        self.assertEqual(Secretary().return_name_person('ъъъъъъ'), False)
    def test_two_return_name_person(self):
        #есть номер в базе
        self.assertEqual(Secretary().return_name_person('10006'), 'Аристарх Павлов')

    def test_one_return_num_shelf(self):
        self.assertEqual(Secretary().return_num_shelf('2207 876234'), '1')
    def test_two_return_num_shelf(self):
        self.assertEqual(Secretary().return_num_shelf('ъъъъ'), False)

    def test_return_list_all(self):
        self.assertEqual(Secretary().return_list_all(), ['passport "2207 876234" "Василий Гупкин"', 'insurance "10006" "Аристарх Павлов"', 'invoice "11-2" "Геннадий Покемонов"'])
    def test_add_doc(self):
        result_doc = Secretary().add_doc(999, 'Тестовый документ', '4', 'Тестовый человек')
        result_dir = directories['4']
        Secretary().del_doc(999)
        self.assertEqual(result_doc, {"type": 'Тестовый документ', "number": 999, "name": 'Тестовый человек'})

    def test_one_add_doc_on_bookshelf_number(self):
        #Обновление полки
        result = Secretary().add_doc_on_bookshelf_number(1278, 3)
        Secretary().del_doc(1278)
        self.assertEqual(result, directories['3'])
    def test_two_add_doc_on_bookshelf_number(self):
        #Добавление полки
        result = Secretary().add_doc_on_bookshelf_number(1333, 4)
        Secretary().del_doc(1333)
        self.assertEqual(result, directories['4'])

    def test_add_shelf(self):
        #Добавление полки
        result = Secretary().add_shelf(13)
        self.assertEqual(result, {str(13) : []})

    def test_del_doc(self):
        #Удаление документа
        doc = {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
        result = Secretary().del_doc(doc['number'])
        documents.append(doc)
        self.assertNotIn(result, [
                                {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
                            ])

    def test_one_deleting_from_directory(self):
        #Удаление полки
        doc = {'2': ['10006']}
        result = Secretary().deleting_from_directory(10006)
        directories.update(doc)
        self.assertNotIn(10006, directories[result])
    def test_two_deleting_from_directory(self):
        #Нет такого номера документа
        self.assertEqual(Secretary().deleting_from_directory(-1), '')


if __name__ == '__main__':
    unittest.main()