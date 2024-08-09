from scr.hh_api_vacancies import HHapiVacancies


def test_hh_api_vacancies(employers):
    """Проверяет типы результата загрузки вакансий"""
    hh_vac = HHapiVacancies()
    vacancies = hh_vac.load_vacancies(employers)
    assert type(vacancies) is list
    assert type(vacancies[0]) is dict
