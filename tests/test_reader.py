import pytest
from unittest.mock import patch
from SkyproPython.src.reader import read_csv_transactions, read_excel_transactions
from SkyproPython.data.transactions_csv import TRANSACTIONS_CSV_PATH
from SkyproPython.data.transactions_excel import TRANSACTIONS_EXCEL_PATH
import pandas as pd


MOCK_CSV_DATA = [
    {'id': 1, 'state': 'EXECUTED', 'to': 'Visa 1234', 'description': 'Перевод с карты на карту'},
    {'id': 2, 'state': 'CANCELED', 'to': 'MasterCard 5678', 'description': 'Открытие вклада'},
    {'id': 3, 'state': 'EXECUTED', 'to': 'Visa 9012', 'description': 'Перевод организации'}
]

MOCK_EXCEL_DATA = [
    {'id': 10, 'state': 'EXECUTED', 'to': 'Discover 0987', 'description': 'Перевод с карты на карту'},
    {'id': 20, 'state': 'CANCELED', 'to': 'American Express 6543', 'description': 'Открытие вклада'},
    {'id': 30, 'state': 'EXECUTED', 'to': 'Visa 2109', 'description': 'Перевод организации'}
]

def test_read_csv_success(mocker):
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame(MOCK_CSV_DATA))
    result = read_csv_transactions()
    assert result == MOCK_CSV_DATA

def test_read_excel_success(mocker):
    mocker.patch('pandas.read_excel', return_value=pd.DataFrame(MOCK_EXCEL_DATA))
    result = read_excel_transactions()
    assert result == MOCK_EXCEL_DATA
