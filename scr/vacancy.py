class Vacancy:
    """Приводит словарь полученный от hh_api_vacancies в рабочее состояние для записи в БД"""
    employer: dict
    vacancy_id: str
    name: str
    salary: dict
    alternate_url: str

    def __init__(self, employer_id, vacancy_id, name, salary, alternate_url):
        self.employer_id = employer_id['id']
        self.vacancy_id = vacancy_id
        self.name = name
        self.salary = salary if salary else {}
        self.pay = self.salary.get('from') if self.salary.get('from') else self.salary.get('to')
        self.alternate_url = alternate_url if alternate_url else '-'

    def __str__(self):
        return f'{self.vacancy_id}, {self.name}, {self.pay}, {self.alternate_url}'

    @classmethod
    def cast_to_object(cls, employers_vacancies):
        """Приводит словарь полученный от hh_api_vacancies в список объектов класса Vacancy"""
        vacancies_list = []
        for employer_vacancies in employers_vacancies:
            for vacancy in employer_vacancies:
                vacancy_object = Vacancy(
                    vacancy.get('employer'),
                    vacancy.get('id'),
                    vacancy.get('name'),
                    vacancy.get('salary'),
                    vacancy.get('alternate_url')
                )
                if vacancy_object.salary != {}:
                    vacancies_list.append(vacancy_object)

        return vacancies_list

    @classmethod
    def cast_object_to_list(cls, vacancies_list):
        vacancies_values = []
        for vacancy in vacancies_list:
            values = [vacancy.employer_id, vacancy.vacancy_id, vacancy.name, vacancy.pay, vacancy.alternate_url]
            vacancies_values.append(values)
