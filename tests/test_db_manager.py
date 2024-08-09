from scr.db_manager import DBManager
from scr.func_converters import *


def test_db_manager_init(db_init):
    """Проверяет создание БД coursework_5"""
    db = DBManager(*db_init)
    result = db.get_from_db('SELECT datname FROM pg_database;')
    assert ('coursework_5',) in result


def test_db_manager_create_table_employers(db_init):
    """Проверяет создание таблицы employers"""
    db = DBManager(*db_init)
    db.create_table_employers()
    tables = db.get_from_db("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    assert ('employers',) in tables


def test_db_manager_employers_columns(db_init):
    """Проверяет названия и порядок колонок таблицы employers"""
    db = DBManager(*db_init)
    db.create_table_employers()
    columns = db.get_from_db("SELECT column_name FROM information_schema.columns "
                             "WHERE table_name = 'employers' "
                             "ORDER BY ordinal_position ASC;")
    assert columns == [('employer_id',), ('name',), ('alternate_url',), ('open_vacancies',)]


def test_db_manager_create_table_vacancies(db_init):
    """Проверяет создание таблицы vacancies"""
    db = DBManager(*db_init)
    db.create_table_employers()
    db.create_table_vacancies()
    tables = db.get_from_db("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    assert ('vacancies',) in tables


def test_db_manager_vacancies_columns(db_init):
    """Проверяет названия и порядок колонок таблицы vacancies"""
    db = DBManager(*db_init)
    db.create_table_employers()
    db.create_table_vacancies()
    columns = db.get_from_db("SELECT column_name FROM information_schema.columns "
                             "WHERE table_name = 'vacancies' "
                             "ORDER BY ordinal_position ASC;")
    assert columns == [('employer_id',), ('vacancy_id',), ('name',), ('pay',), ('alternate_url',)]


def test_db_manager_fill_table_employers(db_created_tables, employers):
    """Проверяет правильность заполнения таблицы employers"""
    db = db_created_tables
    db.fill_table('employers', convert_employers_to_lists(employers))
    result = db.get_from_db('SELECT * FROM employers;')
    assert result[0] == ('1721871', 'Programming Store', 'https://hh.ru/employer/1721871', 48)


def test_db_manager_fill_table_vacancies(db_created_tables, employers, vacancies):
    """Проверяет правильность заполнения таблицы vacancies"""
    db = db_created_tables
    db.fill_table('employers', convert_employers_to_lists(employers))
    db.fill_table('vacancies', convert_vacancies_to_lists(vacancies))
    result = db.get_from_db('SELECT * FROM vacancies;')
    assert result[0] == ('3518049', '104822178', 'Начинающий специалист', 15000, 'https://hh.ru/vacancy/104822178')
