from scr.hh_api_employers import HHapiEmployers


def test_hh_api_employers():
    """Проверка типизации результата метода"""
    hh_emp = HHapiEmployers()
    employers = hh_emp.load_employers(10)
    assert type(employers) is list
    assert type(employers[0]) is dict


def test_hh_api_employers_validation(employers):
    """Проверяет выполнение условия отбора работодателей"""
    for emp in employers:
        assert emp['open_vacancies'] > 0
