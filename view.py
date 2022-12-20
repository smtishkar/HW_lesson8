import uuid

def choose_action():
    print (f"Выберите действие: \nДобавить пользователя - 1\nПоиск пользователя - 2\nУдаление пользователя - 3\nРедактирование пользователя - 4\nВывод списка сотрудников - 5")
    request = int(input('\nВведите значение: '))
    return request

def new_contact():
    name = input("Введите имя: ")
    tel = input("Введите номер: ")
    email = input("Введите должность: ")
    job_role = input("Введите email: ")
    id = str(uuid.uuid4()).split('-')[0]
    # id= id_old[0] 
    return f'{id} || {name} || {tel} || {job_role} || {email}'

def show_found(result):
    print(f'Результат поиска: {result}')


def deleted_contact(result):
    print(f'Пользователь: {result} удален')


def action_for_change():
    print (f"Выберите действие: \nЗаменить телефон - 1\nЗаменить должность - 2\nЗаменить email - 3\n")
    request = int(input('\nВведите значение: '))
    return request