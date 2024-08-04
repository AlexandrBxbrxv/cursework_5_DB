import requests


class HHapiEmployers:
    """Класс для работы с API hh.ru.
    Находит работодателей по запросу 'Программирование'"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/employers'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': 'Программирование', 'page': 0, 'per_page': 20}
        self.__employers = []

    def load_employers(self, number_of_employers: int) -> list:
        """Выбирает указанное количество работодателей,
           количество активных вакансий которых больше 0"""
        print('Выбираем работодателей...')
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            data = response.json()['items']
            self.__employers.extend(data)
            self.__params['page'] += 1

        result = []
        for item in self.__employers:
            if item['open_vacancies'] > 0:
                result.append(item)

        sorted_result = sorted(result, key=lambda x: x['open_vacancies'], reverse=True)
        return sorted_result[:number_of_employers]
