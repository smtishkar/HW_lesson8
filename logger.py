from datetime import datetime as dt
from time import time
import model
import csv

def create_person_logger(contact):
    with open ('database.csv', 'a', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows([contact.split(' || ')])
    with open ('database.txt', 'a', encoding = 'utf-8') as f:
        f.write(f' \n {contact}')



# def get_base():
#     with open ('database.csv', 'a', encoding = 'utf-8') as f:
#         return f.read()

# get_base()