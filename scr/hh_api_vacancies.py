import requests


class HHapiVacancies:
    def __init__(self):

        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__vacancies = []

    def load_vacancies(self, employers):
        for item in employers:
            url_vacancies = item['vacancies_url']
            response = requests.get(url_vacancies, headers=self.__headers)
            data = response.json()['items']
            self.__vacancies.append(data)

        return self.__vacancies


if __name__ == '__main__':
    hh = HHapiVacancies()

    ld_emp = [{'id': '1721871', 'name': 'Programming Store', 'url': 'https://api.hh.ru/employers/1721871',
               'alternate_url': 'https://hh.ru/employer/1721871',
               'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1301046.png',
                             '240': 'https://img.hhcdn.ru/employer-logo/6824447.png',
                             '90': 'https://img.hhcdn.ru/employer-logo/6824446.png'},
               'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1721871', 'open_vacancies': 39},
              {'id': '3518049', 'name': 'Школа программирования и робототехники Пиксель',
               'url': 'https://api.hh.ru/employers/3518049', 'alternate_url': 'https://hh.ru/employer/3518049',
               'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/891581.png',
                             '240': 'https://img.hhcdn.ru/employer-logo/4007012.png',
                             '90': 'https://img.hhcdn.ru/employer-logo/4007011.png'},
               'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3518049', 'open_vacancies': 38}]

    employers = hh.load_vacancies(ld_emp)

    for employer_vacancies in employers:
        for vacancy in employer_vacancies:
            # print(vacancy['employer']['id'], vacancy['id'], vacancy['name'], vacancy['salary'], vacancy['alternate_url'])
            print(vacancy['employer'])
