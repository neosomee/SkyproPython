import requests
import os
from dotenv import load_dotenv
load_dotenv()

def external_api(transaction):
    """
    Конвертирует валюту транзакции в рубли.
    """
    operation_amount = transaction.get('operationAmount')
    if operation_amount is None:
        print("Ошибка: ключ 'operationAmount' отсутствует или равен None")
        return None

    currency = operation_amount.get('currency')
    if currency is None:
        print("Ошибка: ключ 'currency' отсутствует или равен None")
        return None

    code = currency.get('code')
    amount = operation_amount.get('amount')

    if code == 'RUB':
        return float(amount)

    if code in ['EUR', 'USD']:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

            headers = {
                "apikey": os.getenv("API_KEY")
            }

            response = requests.request("GET", url, headers=headers)

            if response.status_code == 200:
                result = response.json()
                converted_amount = result.get('result')
                print(f"Конвертация: {converted_amount} рублей")
                return converted_amount
            else:
                print(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"An error occurred: {e.__class__.__name__} - {str(e)}")

    return None
