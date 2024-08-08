def convert_employers_to_lists(employers: list) -> list[list]:
    """Собирает табличные значения работодателя,
     первая[0] строчка - название колонок таблицы"""
    employers_values_list = []
    header = ['employer_id', 'name', 'alternate_url', 'open_vacancies']
    employers_values_list.append(header)
    for employer in employers:
        employers_values = [
            employer['id'],
            employer['name'],
            employer['alternate_url'],
            employer['open_vacancies']
        ]
        employers_values_list.append(employers_values)
    return employers_values_list


def convert_vacancies_to_lists(employers_vacancies: list) -> list[list]:
    """Собирает табличные значения вакансии,
     выбирает только то вакансии в которых указана минимальная зарплата в рублях,
     первая[0] строчка - название колонок таблицы"""
    vacancies_values_list = []
    header = ['employer_id', 'vacancy_id', 'name', 'pay', 'alternate_url']
    vacancies_values_list.append(header)
    for vacancy in employers_vacancies:
        employer = vacancy.get('employer')
        salary = vacancy.get('salary') if vacancy.get('salary') else {'from': 0, 'currency': 'empty_salary'}
        pay = salary.get('from')
        if pay is None or salary.get('currency') != 'RUR':
            continue
        else:
            vacancy_values = [
                employer.get('id'),
                vacancy.get('id'),
                vacancy.get('name'),
                pay,
                vacancy.get('alternate_url')
            ]
            vacancies_values_list.append(vacancy_values)
    return vacancies_values_list
