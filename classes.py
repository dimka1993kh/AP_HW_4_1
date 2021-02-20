from data import documents, directories
from pprint import pprint

class Secretary():
    def __init__(self):
        pass

    def return_name_person(self, num=False):
        if num == False:
            num=input('Введите номер документа: ')
        person = '';  
        for elem in documents:
            if elem['number'] == num:
                person = elem['name']
                break
        if person == '':
                print('Такого номера нет в базе!') 
                return False
        else:
            print(person)             
            return(person)

    def return_num_shelf(self, num):
        if num == False:
            num = input('Введите номер документа: ')
        bookshelf_number = ''
        print(directories)
        for elem in directories.items():
            if num in elem[1]:
                bookshelf_number = elem[0]
        if len(bookshelf_number) == 0:
            print('Такого номера нет в базе!')
            bookshelf_number = False
        else:
            print(f'Документы находятся на {bookshelf_number} полке')
        return(bookshelf_number)

    def return_list_all(self):
        result = []
        for elem in documents:
            result.append(f'{list(elem.values())[0]} "{list(elem.values())[1]}" "{list(elem.values())[2]}"')
        print(result)
        return result

    def add_doc(self, num_doc=False, type_doc=False, bookshelf_number=False, name_person=False):
        if name_person == False: 
            num_doc = int(input('Введите номер документа: '))
        if type_doc == False: 
            type_doc = input('Введите название документа: ')
        if bookshelf_number == False: 
            bookshelf_number = input('Введите номер полки, куда положить документ: ')
        if name_person == False:    
            name_person = input('Введите имя человека: ')
        documents.append({"type": type_doc, "number": num_doc, "name": name_person})
        self.add_doc_on_bookshelf_number(num_doc, bookshelf_number)
        print(f'Добавлен новый документ: {documents[-1]}')
        return documents[-1]
    
    def add_doc_on_bookshelf_number(self, num, shelf):
        count = 0
        for elem in directories.items(): # Если полка существующая, то она обновится. Если новая, то создастся новая полка.
            if elem[0] == str(shelf):
                elem[1].append(num)
                print(f'Обновлена полка {shelf}')
                count = 1
                break
        if count == 0:
            self.add_shelf(shelf);
            directories[shelf].append(num)
        print(directories[f'{shelf}'])
        return directories[f'{shelf}']

    def add_shelf(self, bookshelf):
        if list(directories.keys()).count(bookshelf) == 0:
            directories.update({str(bookshelf) : []}); # Если полка новая, то создается новая полка. Если полка существующая, то происходит обновление существующей полки
            print(f'Добавлена полка {bookshelf}')
        return {str(bookshelf) : []}

    def del_doc(self, num=False):
        if num == False:
            num = input('Введите номер документа: ')
        bookshelf = ''
        remove_document = ''
        for elem in documents:
            if elem['number'] == num:
                documents.remove(elem)
                remove_document = elem             
                let = self.deleting_from_directory(num)
                print(f'Удален документ с номером: {num} из базы данных и убран с полки №{let}')
        return remove_document

    def deleting_from_directory(self, num):
        bookshelf = ''
        num = str(num)
        for elem in directories.items():
            if num in elem[1]:
                elem[1].remove(num)
                bookshelf = elem[0]
                break
        if bookshelf == '':
            print('Такого номера нет в базе!')
        return bookshelf        

    def move_doc(self, num=False, new_bookshelf=False):
        if num == False:
            num = input('Введите номер документа: ')
        if new_bookshelf == False:
            new_bookshelf = int(input('Введите полку, на которую хотите перенести документ: '))
        bookshelf = self.deleting_from_directory(num)
        self.add_doc_on_bookshelf_number(num, new_bookshelf)
        print(f'Документ №{num} перемещен с полки {bookshelf} на полку {new_bookshelf}')
        return (num, new_bookshelf, bookshelf)

    def end_doc(self):
        work = False
        print('Работа программы окончена')
        return work

    def print_doc(self):
        pprint(documents)
        pprint(directories)
        return True
