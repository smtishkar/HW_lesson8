import csv

def create_person_logger(contact):
    with open ('database.csv', 'a', newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows([contact.split(' || ')])
    with open ('database.txt', 'a', encoding = 'utf-8') as f:
        f.write(f'{contact}\n')

def log_person_change(arr):
    with open('database.csv', 'w', newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for i in arr:
            writer.writerow([i])
    with open ('database.txt', 'w', encoding = 'utf-8') as f:
        for i in arr:
            f.write(f'{i}\n')

def log_delet_person(arr):
    with open('database.csv', 'w', newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for i in arr:
            writer.writerow([i])
    with open ('database.txt', 'w', encoding = 'utf-8') as f:
        for i in arr:
            f.write(f'{i}\n')
