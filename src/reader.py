import pandas as pd

def read_csv_transactions(file_path):
    """
    Чтение CSV-файла.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения CSV: {str(e)}")
        return []

def read_excel_transactions(file_path):
    """
    Чтение Excel-файла.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка чтения Excel: {str(e)}")
        return []

csv_file_path = 'C:\\Users\\Dareshin.D\\Downloads\\transactions.csv'
excel_file_path = 'C:\\Users\\Dareshin.D\\Downloads\\transactions_excel.xlsx'

csv_data = read_csv_transactions(csv_file_path)
excel_data = read_excel_transactions(excel_file_path)