from classes import Secretary

if __name__ == '__main__':

    secr = Secretary()

    command_dict = {'p': secr.return_name_person, 
                    's': secr.return_num_shelf,
                    'l': secr.return_list_all, 
                    'a': secr.add_doc, 
                    'd': secr.del_doc, 
                    'm': secr.move_doc,
                    'as': secr.add_shelf,
                    'end': secr.end_doc, 
                    'print': secr.print_doc
                    };
    try:
        work = ''
        while work != False:
            command = input('Введите команду: ')
            work = command_dict[command]()
    except Exception as err:
        print(err)