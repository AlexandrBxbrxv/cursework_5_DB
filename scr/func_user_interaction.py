from scr.db_manager import DBManager
from scr.hh_api_employers import HHapiEmployers
from scr.hh_api_vacancies import HHapiVacancies
from scr.func_vacancy_converter import *


def generate_and_fill_tables(db):

    hh_emp = HHapiEmployers()
    hh_vac = HHapiVacancies()

    employers = hh_emp.load_employers(15)
    employers_vacancies = hh_vac.load_vacancies(employers)

    db.create_table_employers()
    db.insert_into_table_employers(employers)

    vacancies_list = convert_vacancies_to_lists(employers_vacancies)

    db.create_table_vacancies()
    db.insert_into_table_vacancies(vacancies_list)


def print_table(table: list):
    """Печатает в консоль содержимое таблицы"""
    for row in table:
        print(row)


def user_interaction():
    """Для взаимодействия пользователя с программой"""
    user_input = ''
    if user_input == 'stop':
        exit()
    while user_input not in ('1', '2'):

        user_input = input('Запускаем базу данных\n'
                           '1 - Зайти под стандартным пользователем\n'
                           '2 - Ввести пользователя\n')
        if user_input == '1':
            password = input('Пароль: ') #  'h3K7_f6JH#9oK1U9'
            db = DBManager(password)
        if user_input == '2':
            password = input('Пароль: ')
            user = input('Пользователь: ')
            port = input('Порт: ')
            host = input('Хост: ')
            try:
                db = DBManager(password, user, port, host)
            except Exception:
                print('Что-то введено не правильно')

    while user_input != 'stop':
        generate_and_fill_tables(db)
        print('Работа с базой данных\n'
              '1 - \n'
              '\n'
              '\n'
              '\n'
              '\n')

if __name__ == '__main__':
    pass



