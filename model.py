
from encodings import utf_8

contacts = []
path = 'c:\Python\Seminars\Seminar_telSprav\phonebook.txt'

def read_file():
    global contacts
    with open (path,'r', encoding='utf_8') as f:
        contacts = [i.strip().split('\n') for i in f.readlines() if i != '']
        # contacts = f.readlines()
    print (contacts)

def get_contacts():
    global contacts
    return contacts

def add_contact ():
    global contacts
    # id = input ('Введите id: ')
    name = input ('Введите name: ')
    phone = input ('Введите phone: ')
    comment = input ('Введите comment: ')
    contacts.append (f'{name}, {phone}, {comment}')
    # contacts.append (' | '.join(name, phone, comment))
    
def save_file():
    global contacts
    while True:
            choose_save_option = input (f'Перезаписать текущий файл \
            {path} или сохранить в новом файле? \nN - в новом файле, \n \
            R - перезаписать файл, \nB - отмена\n')
            match choose_save_option:
                case 'N':
                    new_path = input ('Введите название нового файла: ')
                    with open (new_path, 'w', encoding='utf_8') as data:
                        data.write(contacts)
                        print (f'Файл {new_path} сохранен.')
                        break
                case 'R':
                    # with open (path, 'w', encoding='utf_8') as data:
                    #     # data.write(' '.join(contacts))
                    #     data.write("\n".join(map(str, contacts)))
                    #     print (f'Файл {path} сохранен.')
                    with open (path, 'w', encoding='utf_8') as data:
                        # data.write(' '.join(contacts))
                        contacts2 = ''
                        k = 0
                        for i in contacts:
                            k += 1
                            if k >= 2:
                                contacts2 += '\n'
                            for e in i:
                                contacts2 += e
                        print(contacts2)
                        print(type(contacts2))
                        # data.write("\n".join(map(str, contacts)))
                        data.write(contacts2)
                        print (f'Файл {path} сохранен.')
                        break
                case 'B':
                    break   
                case _:  # Аналогично default в других языках
                    print(f"Sorry, I couldn't understand {choose_save_option!r}")

def change_contact():
    # global contacts
    # # myList2 = []
    # # for i in contacts:
    # #     for e in i:
    # #         myList2.append(e.split(','))
    #         # print (e)
    #         # print(contacts)
    # # print(myList2)
    # change_name = input('Введите имя контакта, который хотите изменить: ')
    # bool = True
    # index_change_str = 0
    # for i in range (len(contacts)):
    #     for e in (contacts[i]):
    #         if change_name in contacts[i]:
    #             bool = False
    #             index_change_str = i
    #             # print (e)
    #             # print (i)
    #             break
    # if bool == True:
    #     print ('Совпадений не найдено.')
    # else:
    #     print ('Есть контакт')
    #     new_name = input ('Введите new_name: ')
    #     new_phone = input ('Введите new_phone: ')
    #     new_comment = input ('Введите new_comment: ')
    #     contacts[index_change_str] = [new_name, new_phone, new_comment]
    #     # print (myList2[index_change_str])
    #     change_str = ", ".join(contacts[index_change_str])
    #     contacts[index_change_str] = [change_str]
    # print (change_str)
    # print (myList2)
    # print (contacts)

    global contacts
    myList2 = []
    for i in contacts:
        for e in i:
            myList2.append(e.split(','))
            # print (e)
            # print(contacts)
    print(myList2)
    change_name = input('Введите имя контакта, который хотите изменить: ')
    bool = True
    index_change_str = 0
    for i in range (len(myList2)):
        for e in (myList2[i]):
            if change_name in myList2[i]:
                bool = False
                index_change_str = i
                # print (e)
                # print (i)
                break
    if bool == True:
        print ('Совпадений не найдено.')
    else:
        print ('Есть контакт')
        new_name = input ('Введите new_name: ')
        new_phone = input ('Введите new_phone: ')
        new_comment = input ('Введите new_comment: ')
        myList2[index_change_str] = [new_name, new_phone, new_comment]
        # print (myList2[index_change_str])
    change_str = ", ".join(myList2[index_change_str])
    contacts[index_change_str] = [change_str]
    print (change_str)
    # print (myList2)
    print (contacts)

def del_contact():
    global contacts
    myList2 = []
    for i in contacts:
        for e in i:
            myList2.append(e.split(','))
            # print (e)
            # print(contacts)
    print(myList2)
    del_name = input('Введите имя контакта, который хотите удалить: ')
    bool = True
    index_del_str = 0
    for i in range (len(myList2)):
        for e in (myList2[i]):
            if del_name in myList2[i]:
                bool = False
                index_del_str = i
                # print (e)
                # print (i)
                break
    if bool == True:
        print ('Совпадений не найдено.')
    else:
        print ('Есть контакт')
        # del myList2[index_del_str]
        # print (myList2[index_del_str])
    
    del contacts[index_del_str]

    # print (myList2)
    print (contacts)

def find_contact():
    global contacts
    myList2 = []
    for i in contacts:
        for e in i:
            myList2.append(e.split(','))
            # print (e)
            # print(contacts)
    # print(myList2)
    find_name = input('Введите имя для поиска: ')
    bool = True
    index_find_str = 0
    for i in range (len(myList2)):
        for e in (myList2[i]):
            if find_name in myList2[i]:
                bool = False
                index_find_str = i
                # print (e)
                # print (i)
                break
    if bool == True:
        print ('Совпадений не найдено.')
    else:
        print ('Есть контакт')

    print (contacts[index_find_str])