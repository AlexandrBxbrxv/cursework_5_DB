import requests


class HHapiVacancies:
    """Класс для работы с API hh.ru"""
    def __init__(self):

        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__vacancies = []

    def load_vacancies(self, employers: list) -> list[dict]:
        """Загружает вакансии по ссылке вакансий работодателя,
        принимает список работодателей, возвращает список вакансий"""
        print('Получаем вакансии...')
        for item in employers:
            url_vacancies = item['vacancies_url']
            response = requests.get(url_vacancies, headers=self.__headers)
            data = response.json()['items']
            self.__vacancies.extend(data)

        return self.__vacancies
