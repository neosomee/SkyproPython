import pandas as pd
import pytest
from unittest.mock import patch
from SkyproPython.src.reader import read_csv_transactions, read_excel_transactions

MOCK_CSV_DATA = pd.DataFrame({
    'id': [1, 2, 3],
    'state': ['EXECUTED', 'CANCELED', 'EXECUTED'],
    'to': ['Visa 1234', 'MasterCard 5678', 'Visa 9012'],
    'description': ['Перевод с карты на карту', 'Открытие вклада', 'Перевод организации']
})

MOCK_EXCEL_DATA = pd.DataFrame({
    'id': [10, 20, 30],
    'state': ['EXECUTED', 'CANCELED', 'EXECUTED'],
    'to': ['Discover 0987', 'American Express 6543', 'Visa 2109'],
    'description': ['Перевод с карты на карту', 'Открытие вклада', 'Перевод организации']
})

def test_read_csv_success(mocker):
    """Проверяет успешное чтение CSV-файла."""
    mocker.patch('pandas.read_csv', return_value=MOCK_CSV_DATA)
    result = read_csv_transactions('example.csv')
    pd.testing.assert_frame_equal(result, MOCK_CSV_DATA)

def test_read_excel_success(mocker):
    """Проверяет успешное чтение Excel-файла."""
    mocker.patch('pandas.read_excel', return_value=MOCK_EXCEL_DATA)
    result = read_excel_transactions('example.xlsx')
    pd.testing.assert_frame_equal(result, MOCK_EXCEL_DATA)
