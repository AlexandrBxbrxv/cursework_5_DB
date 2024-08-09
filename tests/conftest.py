import pytest
import json
from config import config_db
from scr.db_manager import DBManager
from scr.func_converters import *


@pytest.fixture()
def employers() -> list[dict]:
    """Возвращает сырые данные по работодателям"""
    with open(r'..\data\employers.json', 'r', encoding='UTF-8') as f:
        result = json.loads(f.read())
    return result


@pytest.fixture()
def vacancies() -> list[dict]:
    """Возвращает сырые данные по вакансиям"""
    with open(r'..\data\test_vacancies.json', 'r', encoding='UTF-8') as f:
        result = json.loads(f.read())
    return result


@pytest.fixture()
def db_init() -> tuple:
    """Возвращает данные подключения к postgresql,
    перед вызовом ставить *"""
    return config_db()


@pytest.fixture()
def db_created_tables(db_init):
    """Возвращает объект класса DBManager, с созданными таблицами"""
    db = DBManager(*db_init)
    db.create_table_employers()
    db.create_table_vacancies()
    return db


@pytest.fixture()
def db_filled_tables(db_created_tables, employers, vacancies):
    """Возвращает объект класса DBManager, с заполненными таблицами"""
    db = db_created_tables
    db.fill_table('employers', convert_employers_to_lists(employers))
    db.fill_table('vacancies', convert_vacancies_to_lists(vacancies))
    return db
