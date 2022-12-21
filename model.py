import csv
import view


def find_person():
    contact = input("Введите имя сотрудника: ")
    base = get_base()
    base = base.split('\n')
    with open ('database.csv', 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for i in base:
            if contact in i:
                print(i)

def delete_person():
    contact = input("id сотрудника: ")
    base = get_base()
    a =[]
    base = base.split('\n')
    for i in base:
        if contact not in i:
            a.append(i)
    return a


def list_employee():
    with open ('database.csv', 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        for i in lst:
            print (i.replace('\n',''))

def get_base():
    with open ('database.txt', 'r', encoding = 'utf-8') as f:
        return f.read()


def person_change():
    contact = input("Введите имя для редактирования сотрудника: ")
    base = get_base()
    a =[]
    base = base.split('\n')
    new_info = view.new_contact()
    for i in base:
        if contact in i:
            i = new_info
            a.append(i)
        else: 
            a.append(i)
    return a
