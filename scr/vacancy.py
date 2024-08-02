class Vacancy:
    """Приводит словарь полученный от hh_api_vacancies в рабочее состояние для записи в БД"""
    employer: dict
    vacancy_id: str
    name: str
    salary: dict
    alternate_url: str

    "вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."

    def __init__(self, employer_id, vacancy_id, name, salary, alternate_url):
        self.employer_id = employer_id['id']
        self.vacancy_id = vacancy_id
        self.name = name
        self.salary = salary if salary else '-'
        self.pay_from = self.salary['from'] if self.salary['from'] else self.salary['to']
        self.alternate_url = alternate_url if alternate_url else '-'

    @classmethod
    def cast_to_object(cls, employers_vacancies):
        """Приводит словарь полученный от hh_api_vacancies в список объектов класса Vacancy"""
        vacancies_list = []
        for employer_vacancies in employers_vacancies:
            for vacancy in employer_vacancies:
                if vacancy.get('salary') is None:
                    continue
                else:
                    vacancy_object = Vacancy(
                        vacancy.get('employer'),
                        vacancy.get('id'),
                        vacancy.get('name'),
                        vacancy.get('salary'),
                        vacancy.get('alternate_url')
                    )
                    vacancies_list.append(vacancy_object)

        return vacancies_list

    @classmethod
    def cast_object_to_list(cls, vacancies_list):
        pass