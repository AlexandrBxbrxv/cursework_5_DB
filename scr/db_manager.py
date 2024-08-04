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
        print('Создаём базу данных coursework_5')
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

    def create_table_employers(self):
        """Создает таблицу employers"""
        conn, cur = self.__connect_to_coursework_5()
        cur.execute('DROP TABLE IF EXISTS employers;'
                    'CREATE TABLE employers'
                    '('
                    'employer_id VARCHAR(20) PRIMARY KEY,'
                    'name VARCHAR(200),'
                    'alternate_url VARCHAR(100),'
                    'open_vacancies SMALLINT'
                    ');')
        conn.commit()
        cur.close()
        conn.close()

    def create_table_vacancies(self):
        """Создает таблицу vacancies"""
        conn, cur = self.__connect_to_coursework_5()
        cur.execute('DROP TABLE IF EXISTS vacancies;'
                    'CREATE TABLE vacancies'
                    '('
                    'employer_id VARCHAR(20),'
                    'vacancy_id VARCHAR(20) PRIMARY KEY,'
                    'name TEXT,'
                    'pay INT,'
                    'alternate_url VARCHAR(200),'
                    'FOREIGN KEY (employer_id) REFERENCES employers(employer_id)'
                    ');')
        conn.commit()
        cur.close()
        conn.close()

    def insert_into_table_employers(self, dicts_list: list):
        """Заполняет таблицу employers, на вход принимает список словарей."""
        conn, cur = self.__connect_to_coursework_5()

        table_columns = 'employer_id, name, alternate_url, open_vacancies'

        for item in dicts_list:
            query = f'INSERT INTO employers ({table_columns}) VALUES ({', '.join(['%s'] * 4)});'
            values = [item['id'], item['name'], item['alternate_url'], item['open_vacancies']]
            cur.execute(query, values)

        conn.commit()
        cur.close()
        conn.close()
        print(f'Данные успешно загружены в таблицу employers')

    def insert_into_table_vacancies(self, values_list: list):
        """Заполняет таблицу vacancies, на вход принимает список значений."""
        conn, cur = self.__connect_to_coursework_5()

        table_columns = 'employer_id, vacancy_id, name, pay, alternate_url'

        for value in values_list:
            query = f'INSERT INTO vacancies ({table_columns}) VALUES ({', '.join(['%s'] * 5)});'
            cur.execute(query, value)

        conn.commit()
        cur.close()
        conn.close()
        print(f'Данные успешно загружены в таблицу vacancies')

    def select_from_table(self, columns: str, table_name: str) -> list:
        """Возвращает выбранные колонки указанной таблицы.
        Выбор как в sql * или название колонок через запятую"""
        conn, cur = self.__connect_to_coursework_5()

        cur.execute(f'SELECT {columns} FROM {table_name};')
        result = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()
        return result

    def get_all_vacancies(self) -> list:
        """Возвращает список всех вакансий с колонками:
        названия компании, названия вакансии, зарплаты, ссылки на вакансию"""
        conn, cur = self.__connect_to_coursework_5()

        cur.execute('SELECT employers.name AS employer_name, vacancies.name, vacancies.pay, vacancies.alternate_url'
                    'FROM vacancies'
                    'INNER JOIN employers USING(employer_id);')
        result = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()
        return result

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """Возвращает список всех вакансий,
        в названии которых содержатся переданные в метод слова"""
        conn, cur = self.__connect_to_coursework_5()

        cur.execute(f'SELECT *' 
                    f'FROM vacancies'
                    f'WHERE name LIKE "%{keyword}%";')
        result = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()
        return result

    def get_companies_and_vacancies_count(self) -> list:
        """Возвращает список всех компаний и количество вакансий у каждой компании"""
        conn, cur = self.__connect_to_coursework_5()

        cur.execute('SELECT employers.name AS employer_name, COUNT(vacancies.name) AS vacancies_amount'
                    'FROM employers'
                    'INNER JOIN vacancies USING(employer_id)'
                    'GROUP BY employers.name'
                    'ORDER BY vacancies_amount DESC;')
        result = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()
        return result
