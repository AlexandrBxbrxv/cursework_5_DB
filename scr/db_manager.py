import psycopg2


class DBManager:
    """Для создания и работы с базой данных coursework_5"""
    user: str
    password: str
    port: str
    host: str

    # !!!ВНИМАНИЕ!!! перед сдачей убери пароль
    # !!!ВНИМАНИЕ!!! перед сдачей убери пароль
    # !!!ВНИМАНИЕ!!! перед сдачей убери пароль
    def __init__(self, password='h3K7_f6JH#9oK1U9', user='postgres', port='5432', host='localhost'):
        """Можно указать данные вашего подключения, если оставить пустым - подключится к postgres.
        Поле password - обязательно для заполнения"""
        # !!!ВНИМАНИЕ!!! перед сдачей убери пароль# !!!ВНИМАНИЕ!!! перед сдачей убери пароль
        # !!!ВНИМАНИЕ!!! перед сдачей убери пароль# !!!ВНИМАНИЕ!!! перед сдачей убери пароль
        # !!!ВНИМАНИЕ!!! перед сдачей убери пароль# !!!ВНИМАНИЕ!!! перед сдачей убери пароль

        self.user = user
        self.password = password
        self.port = port
        self.host = host

        self.__create_database_coursework_5()

    def __create_database_coursework_5(self):
        """Создает базу данных coursework_5"""
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

    def __connect_to_coursework_5(self):
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
                    'id SMALLINT PRIMARY KEY,'
                    'name VARCHAR(100),'
                    'alternate_url VARCHAR(100),'
                    'vacancies_url VARCHAR(100),'
                    'open_vacancies SMALLINT'
                    ');')
        conn.commit()
        cur.close()
        conn.close()

    def insert_into_table_employers(self, values_list):
        """Заполняет таблицу employers, на вход принимает список словарей."""
        conn, cur = self.__connect_to_coursework_5()

        table_columns = 'id, name, alternate_url, vacancies_url, open_vacancies'

        for item in values_list:
            query = f'INSERT INTO employers ({table_columns}) VALUES ({', '.join(['%s'] * len(item.values() - 2))})'
            cur.execute(query, item.values())
        conn.commit()
        cur.close()
        conn.close()
        print(f'Данные успешно загружены в таблицу employers')
