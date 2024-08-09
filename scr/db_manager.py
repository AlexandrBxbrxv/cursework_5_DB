import psycopg2


class DBManager:
    """Для создания и работы с базой данных coursework_5"""
    user: str
    password: str
    port: str
    host: str

    def __init__(self, password='12345', user='postgres', port='5432', host='localhost'):
        """Можно указать данные вашего подключения, если оставить пустым - подключится к postgres.
        Поле password - обязательно для заполнения"""

        self.user = user
        self.password = password
        self.port = port
        self.host = host

        self.__create_database_coursework_5()

    def __create_database_coursework_5(self):
        """Создает базу данных coursework_5"""
        print('Пытаемся зайти в базу данных...')
        conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            port=self.port,
            host=self.host
        )
        curr = conn.cursor()

        conn.autocommit = True
        curr.execute('DROP DATABASE IF EXISTS coursework_5')
        curr.execute('CREATE DATABASE coursework_5')
        conn.autocommit = False

        curr.close()
        conn.close()

    def __connect_to_coursework_5(self) -> tuple:
        """Подключение к БД, возвращает: connector, cursor"""
        conn = psycopg2.connect(
            dbname='coursework_5',
            user=self.user,
            password=self.password,
            port=self.port,
            host=self.host
        )
        return conn, conn.cursor()

    def __execute_query(self, query: str):
        """Метод для сокращения одинаковых функций,
        посылает в базу данных запрос query"""
        conn, cur = self.__connect_to_coursework_5()
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()

    def __fetch_all(self, query: str):
        """Метод для сокращения одинаковых функций,
        возвращает из базы данных результат запроса query"""
        conn, cur = self.__connect_to_coursework_5()
        cur.execute(query)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    def create_table_employers(self):
        """Создает таблицу employers"""
        query = ('DROP TABLE IF EXISTS employers;'
                 'CREATE TABLE employers'
                 '('
                 'employer_id VARCHAR(20) PRIMARY KEY,'
                 'name VARCHAR(200),'
                 'alternate_url VARCHAR(100),'
                 'open_vacancies SMALLINT'
                 ');')
        self.__execute_query(query)

    def create_table_vacancies(self):
        """Создает таблицу vacancies"""
        query = ('DROP TABLE IF EXISTS vacancies;'
                 'CREATE TABLE vacancies'
                 '('
                 'employer_id VARCHAR(20),'
                 'vacancy_id VARCHAR(20) PRIMARY KEY,'
                 'name TEXT,'
                 'pay INT,'
                 'alternate_url VARCHAR(200),'
                 'FOREIGN KEY (employer_id) REFERENCES employers(employer_id)'
                 ');')
        self.__execute_query(query)

    def fill_table(self, table_name: str, values_list: list[list]):
        """Заполняет таблицу в БД coursework_5, на вход принимает название таблицы и список списков_значений,
         первой строкой списка должен быть список названий колонок таблицы."""
        conn, cur = self.__connect_to_coursework_5()

        header = values_list[0]

        for value in values_list[1:]:
            query = f'INSERT INTO {table_name} ({", ".join(header)}) VALUES ({', '.join(['%s'] * len(header))});'
            cur.execute(query, value)

        conn.commit()
        cur.close()
        conn.close()
        print(f'Данные успешно загружены в таблицу {table_name}')

    # Методы из задания для взаимодействия с пользователем

    def get_all_vacancies(self) -> list:
        """Возвращает список всех вакансий с колонками:
        названия компании, названия вакансии, зарплаты, ссылки на вакансию"""

        query = ('SELECT employers.name AS employer_name, vacancies.name, vacancies.pay, vacancies.alternate_url '
                 'FROM vacancies '
                 'INNER JOIN employers USING(employer_id);')
        return self.__fetch_all(query)

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """Возвращает список всех вакансий,
        в названии которых содержатся переданные в метод слова"""

        query = f"SELECT * FROM vacancies WHERE vacancies.name LIKE '%{keyword}%';"
        return self.__fetch_all(query)

    def get_companies_and_vacancies_count(self) -> list:
        """Возвращает список всех компаний и количество вакансий у каждой компании"""

        query = ('SELECT employers.name AS employer_name, COUNT(vacancies.name) AS vacancies_amount '
                 'FROM employers '
                 'INNER JOIN vacancies USING(employer_id) '
                 'GROUP BY employers.name '
                 'ORDER BY vacancies_amount DESC;')
        return self.__fetch_all(query)

    def get_avg_salary(self) -> int:
        """Возвращает среднюю зарплату по вакансиям"""

        query = 'SELECT AVG(pay) FROM vacancies;'
        return round(self.__fetch_all(query)[0][0])

    def get_vacancies_with_higher_salary(self) -> list:
        """Возвращает список всех вакансий, зарплата которых выше средней по всем вакансиям"""

        query = (f'SELECT * FROM vacancies '
                 f'WHERE pay > {self.get_avg_salary()}')
        return self.__fetch_all(query)

    def get_from_db(self, query: str):
        """Метод для тестирования,
        возвращает результат sql запроса отправленного в аргумент метода"""
        return self.__fetch_all(query)
