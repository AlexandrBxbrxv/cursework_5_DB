from scr.func_converters import *


def test_func_convert_employers_header(employers):
    """Проверяет правильность заголовка списка, для форматирования в столбцы таблицы employers"""
    header = convert_employers_to_lists(employers)[0]
    assert type(header) is list
    table_columns = ", ".join(header)
    assert table_columns == 'employer_id, name, alternate_url, open_vacancies'


def test_func_convert_employers_row_attributes(employers):
    """Проверяет порядок значений"""
    first_row = convert_employers_to_lists(employers)[1]
    assert type(first_row) is list
    assert first_row == ['1721871', 'Programming Store', 'https://hh.ru/employer/1721871', 48]


def test_func_convert_vacancies_header(vacancies):
    """Проверяет правильность заголовка списка, для форматирования в столбцы таблицы vacancies"""
    header = convert_vacancies_to_lists(vacancies)[0]
    assert type(header) is list
    table_columns = ", ".join(header)
    assert table_columns == 'employer_id, vacancy_id, name, pay, alternate_url'


def test_func_convert_vacancies_row_attributes(vacancies):
    """Проверяет порядок значений"""
    first_row = convert_vacancies_to_lists(vacancies)[1]
    assert type(first_row) is list
    assert first_row == ['3518049', '104822178', 'Начинающий специалист', 15000, 'https://hh.ru/vacancy/104822178']


def test_func_convert_vacancies_validation(employers):
    """Проверяет выполнение условия отбора вакансий"""
    vacancies = convert_vacancies_to_lists(employers)
    for vac in vacancies[1:]:
        assert vac[3] > 0  # на этой позиции стоит заплата int

