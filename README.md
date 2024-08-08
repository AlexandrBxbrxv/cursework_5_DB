  Программа подключается к PostgreSQL, создает базу данных coursework_5_DB, 
если на вашем сервере установлено ограничение по подключениям отключитесь от сервера перед запуском программы.
  Затем находит минимум 10 работодателей на сайте hh.ru по запросу "Программирование" количество вакансий которых больше нуля,
получает их вакансии, создаёт соответствующие таблицы в БД coursework_5_DB и заполняет их полученными данными.
  После чего можно вывести данные этих таблиц из программы, на выбор 5 методов вывода:
1. Список всех компаний и количество вакансий у каждой компании.
2. Все вакансии.
3. Средняя зарплата по вакансиям.
4. Вакансии, зарплата которых выше средней по всем вакансиям.
5. Вакансии в названии которых содержатся переданные слова.

Программа поддерживается на python 3.12.3 и выше, запускается из файла main.py