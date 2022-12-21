import csv
# from csv import writer
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
    # contact = input("Введите имя сотрудника: ")
    contact = input("id сотрудника: ")
    base = get_base()
    a =[]
    base = base.split('\n')
    for i in base:
        if contact not in i:
            a.append(i)
    # print(a)
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
    # print(base)
    base = base.split('\n')
    # print(base)
    new_info = view.new_contact()
    for i in base:
        if contact in i:
            i = new_info
            a.append(i)
        else: 
            a.append(i)
    # print(a)
    return a


# def find_person():
#     with open ('database.txt', 'r', encoding = 'utf-8') as f:
#         lst = f.readlines()
#         print (lst)
#         result = []
#         flag = True
#         find = input("Введите имя сотрудника: ")
#         for i in lst:
#             if find in i:
#                 result.append(i)
#                 print (i.replace('\n',''))
#                 flag = False
#         if flag:
#             print ("Контакт не найден")
   
#     return result



# def delete_person():
#     find = input("Введите имя сотрудника: ")
#     base = open ('database.csv', 'r+')
#     file_content = base.readlines()
#     found = False
#     for line in file_content:
#         if find in line:
#             found = True
#             file = open ('database.csv', 'r')
#             f = file.read().replace(line,'')
#             file2 = open('database.csv', 'w')
#             file2.write(f)
#             file.close()
#     return find


# def get_base():
#     a = []
#     with open ('database.csv', 'r', encoding = 'utf-8') as f:
#         reader = csv.reader(f, delimiter=';')
#         for row in reader:
#             a.append(row)
#         # print(a)    
#     return a 
# #         # return f.read()


# def list_employee():
#     with open ('database.txt', 'r', encoding = 'utf-8') as f:
#         lst = f.readlines()
#         for i in lst:
#             print (i.replace('\n',''))