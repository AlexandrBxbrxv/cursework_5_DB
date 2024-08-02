import requests


class HHapiEmployers:
    """Находит работодателей по запросу 'Программирование'"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/employers'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': 'Программирование', 'page': 0, 'per_page': 20}
        self.__employers = []

    def load_employers(self, number_of_employers: int):
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


ld_emp = [{'id': '1721871', 'name': 'Programming Store', 'url': 'https://api.hh.ru/employers/1721871', 'alternate_url': 'https://hh.ru/employer/1721871', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1301046.png', '240': 'https://img.hhcdn.ru/employer-logo/6824447.png', '90': 'https://img.hhcdn.ru/employer-logo/6824446.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1721871', 'open_vacancies': 39}, {'id': '3518049', 'name': 'Школа программирования и робототехники Пиксель', 'url': 'https://api.hh.ru/employers/3518049', 'alternate_url': 'https://hh.ru/employer/3518049', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/891581.png', '240': 'https://img.hhcdn.ru/employer-logo/4007012.png', '90': 'https://img.hhcdn.ru/employer-logo/4007011.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3518049', 'open_vacancies': 38}]

table_columns = ld_emp[0].keys()

print(*ld_emp[0].keys())
