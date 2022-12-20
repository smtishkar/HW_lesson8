import csv
from csv import writer
import view

def find_person():
    with open ('database.txt', 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        print (lst)
        result = []
        flag = True
        find = input("Введите имя сотрудника: ")
        for i in lst:
            if find in i:
                result.append(i)
                print (i.replace('\n',''))
                flag = False
        if flag:
            print ("Контакт не найден")
   
    return result

def delete_person():
    find = input("Введите имя сотрудника: ")
    base = open ('database.csv', 'r+')
    file_content = base.readlines()
    found = False
    for line in file_content:
        if find in line:
            found = True
            file = open ('database.csv', 'r')
            f = file.read().replace(line,'')
            file2 = open('database.csv', 'w')
            file2.write(f)
            file.close()


def person_change():
    find = input("Введите имя сотрудника: ")
    change = view.action_for_change()
    with open('database.csv', 'r') as inp, open('new_database.csv', 'w', encoding = 'utf-8') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            row = str(row).split ('||')
            print (find, row[1])
            print (type(find))
            print (type (row[1]))
            if find == row [1]:
                writer.writerow(row)
            elif find != row [1] :
                print('ffffffffff')
                if change == 1:
                    row [2] = input("Введите новый номер: ")
                    writer.writerow(row)
                if change == 2:
                    row [3] = input("Введите новую должность: ")
                    writer.writerow(row)
                if change == 3:
                    row [4] = input("Введите новый email: ")   
                    writer.writerow(row)



# def person_change():
#     find = input("Введите имя сотрудника: ")
#     change = view.action_for_change()
#     with open('database.csv', 'r') as inp, open('new_database.csv', 'w', encoding = 'utf-8') as out:
#         writer = csv.writer(out)
#         for row in csv.reader(inp):
#             row = str(row).split ('||')
#             print(find, row[1])
#             if find != row [1]:
#                 # print ('Yes')
#                 writer.writerow(row)
#             else:
#                 if change == 1:
#                     row [2] = input("Введите новый номер: ")
#                     writer.writerow(row)
#                 if change == 2:
#                     row [3] = input("Введите новую должность: ")
#                     writer.writerow(row)
#                 if change == 3:
#                     row [4] = input("Введите новый email: ")   
#                     writer.writerow(row)


# def person_change():
#     find = input("Введите имя сотрудника: ")
#     # change = view.action_for_change() 
#     with open ('database.csv', 'r+') as f:
#         for line in f:
#             if find in line:

#                 line.split('||')[1] = '3333'
#                 print (line.split('||')[1])

    
# with open('database.csv') as source, open('new_database.csv',"w",newline="") as result:
# reader = csv.reader(source)
# writer = csv.writer(result)
# for line in reader:
# # for mod in module_names:
#     if any([mod in s for s in line]):
#         line.replace(reader[4],mod)
#         print ("YES")
#     writer.writerow("OUT")
#     print (mod)
# module_names.seek(0)
# lines=reader


# def person_change():
#     find = input("Введите имя сотрудника: ")
#     # change = view.action_for_change() 
#     with open ('database.csv') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             base = str(row).split('||')
#             print(base) 
#             if find in row:
#                 with open ('new_database.csv', 'w') as f:
#                     writer = csv.writer(f)
#                     for line in lines:
#                         w



# person_change()


def list_employee():
    with open ('database.txt', 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        for i in lst:
            print (i.replace('\n',''))

