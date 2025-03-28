import pandas as pd


def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path, sep=';')

        print("Размерность датафрейма:", df.shape)
        print("Первые строки датафрейма:\n", df.head())

        return df

    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return None


csv_file_path = 'C:\\Users\\Dareshin.D\\Downloads\\transactions.csv'
df = read_csv_file(csv_file_path)


def read_excel_file(file_path1):
    try:
        df1 = pd.read_excel(file_path1)

        print("Размерность датафрейма:", df1.shape)
        print("Первые строки датафрейма:\n", df1.head())

        return df1

    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return None


excel_file_path = 'C:\\Users\\Dareshin.D\\Downloads\\transactions_excel.xlsx'
df1 = read_excel_file(excel_file_path)
