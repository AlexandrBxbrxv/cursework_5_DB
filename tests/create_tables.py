from scr.db_manager import DBManager
from scr.hh_api_employers import HHapiEmployers
from scr.hh_api_vacancies import HHapiVacancies
from scr.func_vacancy_converter import *


if __name__ == '__main__':

    hh_emp = HHapiEmployers()
    hh_vac = HHapiVacancies()
    db = DBManager()

    # Получение списка словарей работодателей
    employers = hh_emp.load_employers(10)

    # Получение списка словарей вакансий работодателей
    employers_vacancies = hh_vac.load_vacancies(employers)
    # Конвертация полученного в список списков целевых значений вакансий
    vacancies_list = convert_vacancies_to_lists(employers_vacancies)

    # Создание и заполнение таблицы employers
    db.create_table_employers()
    db.insert_into_table_employers(employers)

    # Создание и заполнение таблицы vacancies
    db.create_table_vacancies()
    db.insert_into_table_vacancies(vacancies_list)

    # Вывод таблиц
    print('-')
    table_employers = db.select_from_table('*', 'employers')
    for row in table_employers:
        print(row)
    print('-\n-\n-')
    table_vacancies = db.select_from_table('*', 'vacancies')
    for row in table_vacancies:
        print(row)
