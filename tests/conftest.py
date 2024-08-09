import pytest
import json


@pytest.fixture()
def employers() -> list[dict]:
    """Возвращает сырые данные по работодателям"""
    with open(r'C:\Users\Alexsandr\PycharmProjects\new_coursework_5_DB\data\employers.json', 'r', encoding='UTF-8') as f:
        result = json.loads(f.read())
    return result


@pytest.fixture()
def vacancies() -> list[dict]:
    """Возвращает сырые данные по вакансиям"""
    with open(r'C:\Users\Alexsandr\PycharmProjects\new_coursework_5_DB\data\test_vacancies.json', 'r', encoding='UTF-8') as f:
        result = json.loads(f.read())
    return result
