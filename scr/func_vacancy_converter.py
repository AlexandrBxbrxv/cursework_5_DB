def convert_vacancies_to_lists(employers_vacancies):
    """Собирает основные значения вакансии,
     выбирает только то вакансии в которых указана минимальная зарплата в рублях"""
    vacancies_values = []
    for employer_vacancies in employers_vacancies:
        for vacancy in employer_vacancies:
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
                vacancies_values.append(vacancy_values)
    return vacancies_values
