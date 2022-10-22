
def show_menu():
    question = 'Введите необходимую команду: \n\
        \n 1. Показать все контакты\
        \n 2. Открыть файл с контактами\
        \n 3. Записать файл с контактами\
        \n 4. Добавить контакт\
        \n 5. Изменить контакт\
        \n 6. Удалить контакт\
        \n 7. Поиск по контактам\
        \n 0. Выход.\
        \n' 
    соmmand = input (question)
    return соmmand

def show_contacts(contacts):
    for i in contacts:
            print (i)
    print(contacts)
    # print ([(contact) for contact in contacts])
# show_contacts(myList)

