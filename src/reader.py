import pandas as pd
from SkyproPython.data.transactions_csv import TRANSACTIONS_CSV_PATH
from SkyproPython.data.transactions_excel import TRANSACTIONS_EXCEL_PATH

def read_csv_transactions():
    """Чтение CSV-файла"""
    try:
        df = pd.read_csv(TRANSACTIONS_CSV_PATH)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения CSV: {str(e)}")
        return []

def read_excel_transactions():
    """Чтение Excel-файла с обработкой ошибок"""
    try:
        df = pd.read_excel(TRANSACTIONS_EXCEL_PATH)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения Excel: {str(e)}")
        return []
