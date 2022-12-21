from datetime import datetime as dt
from time import time
import model
import csv

def create_person_logger(contact):
    with open ('database.csv', 'a', newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows([contact.split(' || ')])
    with open ('database.txt', 'a', encoding = 'utf-8') as f:
        # f.write(f' \n {contact}')
        f.write(f'{contact}\n')

def log_person_change(arr):
    with open('database.csv', 'w', newline='', encoding = 'utf-8') as f:
        # csv_a = [i.split(' || ') for i in a]
        writer = csv.writer(f, delimiter=';')
        for i in arr:
            writer.writerow([i])
    with open ('database.txt', 'w', encoding = 'utf-8') as f:
        for i in arr:
            f.write(f'{i}\n')
        # f.write(f' \n {contact}')
        


def log_delet_person(arr):
    with open('database.csv', 'w', newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for i in arr:
            writer.writerow([i])
    with open ('database.txt', 'w', encoding = 'utf-8') as f:
        for i in arr:
            f.write(f'{i}\n')
    # f.write(f' \n {contact}')
        


# def get_base():
#     with open ('database.csv', 'a', encoding = 'utf-8') as f:
#         return f.read()

# get_base()