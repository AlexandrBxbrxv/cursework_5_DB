from scr.db_manager import DBManager
from scr.hh_api_employers import HHapiEmployers
from scr.hh_api_vacancies import HHapiVacancies
from scr.func_converters import *


def generate_and_fill_tables(db):
    """Поучает работодателей и их вакансии, создаёт соответствующие таблицы и заполняет их"""
    hh_emp = HHapiEmployers()
    hh_vac = HHapiVacancies()

    employers = hh_emp.load_employers(10)
    vacancies = hh_vac.load_vacancies(employers)

    db.create_table_employers()
    db.fill_table('employers', convert_employers_to_lists(employers))

    db.create_table_vacancies()
    db.fill_table('vacancies', convert_vacancies_to_lists(vacancies))


def print_table(table: list):
    """Печатает в консоль содержимое таблицы"""
    print(f'-\nДлинна списка: {len(table)}'
          f'\n')
    for row in table:
        print(row)


def user_interaction():
    """Для взаимодействия пользователя с программой"""
    user_input = ''
    is_authorized = False

    while not is_authorized:
        if user_input == 'stop':
            exit()
        user_input = input('-\nАвторизуйтесь в базе данных\n'
                           '1 - Зайти под стандартным пользователем\n'
                           '2 - Ввести пользователя\n'
                           'stop - Прекратить работу\n')
        if user_input == '1':
            password = input('Пароль: ')
            try:
                db = DBManager(password)
                print('Создана база данных coursework_5')
                is_authorized = True
            except Exception:
                print('Не верный пароль')

        if user_input == '2':
            password = input('Пароль: ')
            user = input('Пользователь: ')
            port = input('Порт: ')
            host = input('Хост: ')
            try:
                db = DBManager(password, user, port, host)
                print('Создана база данных coursework_5')
                is_authorized = True
            except Exception:
                print('Что-то введено не правильно')

    generate_and_fill_tables(db)

    while user_input != 'stop':

        user_input = input('-\nРабота с базой данных\n'
                           '1 - Список всех компаний и количество вакансий у каждой компании\n'
                           '2 - Все вакансии\n'
                           '3 - Средняя зарплата по вакансиям\n'
                           '4 - Вакансии, зарплата которых выше средней по всем вакансиям\n'
                           '5 - Вакансии, в названии которых содержатся переданные слова\n'
                           'stop - Прекратить работу\n')

        if user_input == '1':
            print_table(db.get_companies_and_vacancies_count())
        if user_input == '2':
            print_table(db.get_all_vacancies())
        if user_input == '3':
            print(f'{db.get_avg_salary()} рублей')
        if user_input == '4':
            print_table(db.get_vacancies_with_higher_salary())
        if user_input == '5':
            user_word = input()
            print_table(db.get_vacancies_with_keyword(user_word))
