import requests


class HHapiVacancies:
    def __init__(self):

        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__vacancies = []

    def load_vacancies(self, employers):
        print('Получаем вакансии...')
        for item in employers:
            url_vacancies = item['vacancies_url']
            response = requests.get(url_vacancies, headers=self.__headers)
            data = response.json()['items']
            self.__vacancies.append(data)

        return self.__vacancies
