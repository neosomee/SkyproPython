## Описание проекта

Данный проект представляет собой набор утилит для обработки и маскирования данных банковских карт и счетов. Он включает функции для фильтрации и сортировки транзакций, а также для маскирования номеров карт и счетов, чтобы обеспечить безопасность и конфиденциальность пользователей.

## Структура проекта

Проект состоит из нескольких файлов, каждый из которых отвечает за определённые функции:

- `processing.py`: функции для фильтрации и сортировки данных.
- `masks.py`: функции для маскирования номеров карт и счетов.
- `widget.py`: вспомогательные функции для работы с данными.
- `main.py`: основной файл, который демонстрирует использование функций.

## Функции

### Файл: `processing.py`

- **filter_by_state(data, state='EXECUTED')**
  - Фильтрует список словарей по значению ключа `state`.
  - Возвращает новый список словарей с указанным состоянием.

- **sort_by_date(data, descending=True)**
  - Сортирует список словарей по дате.
  - Возвращает новый отсортированный список.

### Файл: `masks.py`

- **get_mask_card_number(card_number: str) -> str**
  - Маскирует номер банковской карты, показывая первые 6 и последние 4 цифры.
  
- **get_mask_account(account_number: str) -> str**
  - Маскирует номер банковского счета, отображая только последние 4 цифры.

### Файл: `widget.py`

- **mask_account_card(account_info)**
  - Маскирует номер карты или счета, показывая только часть информации.
  
- **get_date(date_str)**
  - Преобразует строку даты в более удобный формат (дд.мм.гггг).

### Файл: `generators.py`
- **def filter_by_currency(transactions, currency_code)**
  - Эта функция фильтрует список транзакций по заданному коду валюты. 
- **def transaction_descriptions(transactions)**
  - Функция возвращает описание каждой транзакции из списка. 
- **def card_number_generator(first_numb: int, second_numb: int)**
  - Эта функция генерирует номера карт в указанном диапазоне.
    

### Файл: `main.py`

Основной файл, который демонстрирует работу всех функций. В нём выполняются следующие действия:
- Маскирование номера карты и счета.
- Демонстрация работы с массивом карточек.
- Форматирование даты.

## Пример использования

Для запуска программы просто выполните файл `main.py`. Программа продемонстрирует:
1. Маскирование номера карты.
2. Маскирование номера счета.
3. Маскирование различных типов карт и счетов.
4. Форматирование даты.

### Пример вывода:

- Маскированный номер карты: 700079 ** **** 6361
- Маскированный номер счета: **7305
- Visa Platinum 7000 ** **** 6361
- Maestro 7000 ** **** 6361
- Счет **7305
- 11.03.2024

## Тестирование

Проект содержит набор тестов, написанных с использованием библиотеки `pytest`, для проверки корректности работы функций. Тесты охватывают следующие аспекты:

-   Проверка преобразования даты.
-   Проверка маскирования номера карты.
-   Проверка маскирования номера счета.
-   Проверка фильтрации операций по статусу.
-   Проверка сортировки операций по дате.
-   Тестирует функции фильтрации транзакций и генерации номеров карт.

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

## Зависимости

- Для запуска тестов необходимо установить библиотеку `pytest`. Это можно сделать с помощью следующей команды: `pytest`

