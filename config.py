from configparser import ConfigParser


def config_db(file_name: str = r'C:\Users\Alexsandr\PycharmProjects\new_coursework_5_DB\database.ini') -> tuple:
    """Конфиг специально настроен для работы с классом DBManager,
    возвращает 4 значения необходимые для инициализации,
    перед функцией ставить * для распаковки значений"""
    parser = ConfigParser()
    parser.read(file_name)
    db = {}
    if parser.has_section('postgresql'):
        params = parser.items('postgresql')
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in {1} file.'.format('postgresql', file_name)
        )
    return db['password'], db['user'], db['port'], db['host']
