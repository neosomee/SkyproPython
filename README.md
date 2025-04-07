## Описание проекта

Данный проект представляет собой набор утилит для обработки и маскирования данных банковских карт и счетов. Он включает функции для фильтрации и сортировки транзакций, а также для маскирования номеров карт и счетов, чтобы обеспечить безопасность и конфиденциальность пользователей.



## Структура проекта

Проект имеет c тестированием теперь следующую структуру:

-   `data/`: Содержит данные для функций src директории.
    -   `operations.json`: Данные для функции utils.py.
    -   `transactions.csv`: Данные csv для функции reader.py.
    -   `transactions_excel.xlsx`: Данные excel для функции reader.py.
    -   `transactions_csv.py`: Нахождение файла transactions.csv.
    -   `transactions_excel.py`: Нахождение файла transactions_excel.xlsx.
    

-   `logs/`: Содержит логи для функций src директории.
    -   `masks.log`: Логи файла masks.py
    -   `utils.log`: Логи файла utils.py


-   `src/`: Содержит исходный код проекта.
    -   `widget.py`: Содержит функции для форматирования даты и маскирования номера счета в виджете.
    -   `processing.py`: Содержит функции для фильтрации и сортировки операций.
    -   `masks.py`: Содержит функции для маскирования номеров карт и счетов.
    - `__init__.py` : Для маркировки директории как Python-пакета.
    - `generators.py` : Фильтрует транзакции, генерирует описания и номера карт.
    - `decorators.py` : Записывает информацию о вызовах функций.
    - `external_api.py` : Конвертирует валюту в рубли.
    - `reader.py` : Считывает csv и excel файлы.
    - `search_reader.py` : Возвращает список словарей


-   `tests/`: Содержит тесты для проекта.
    -   `test_widget.py`: Содержит тесты для функций из `widget.py`.
    -   `test_processing.py`: Содержит тесты для функций из `processing.py`.
    -   `test_mask.py`: Содержит тесты для функций из `masks.py`.
    -   `__init__.py` : Для маркировки директории как Python-пакета
    -   `test_generators.py` : Тестирует функции фильтрации транзакций и генерации номеров карт.
    -   `test_decorators.py` : Тестирует функции записывания информации о вызовах функций.
    -   `test_decorators.py` : Тестирует функции записывания информации о вызовах функций.
    -   `test_external_api.py` : Тестирует функции конвертирования валюты в рубли.
    -   `test_reader.py` : Тестирует функции cчитывания csv и excel файлы.
    -   `test_search_reader.py` : Тестирует функции возвращения списка словарей.


-   `main.py`: Отвечает за основную логику проекта и связывает функциональности между собой.

## Зависимости

- Для запуска тестов необходимо установить библиотеку `pytest`. Это можно сделать с помощью следующей команды: `pytest`

