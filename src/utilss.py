import json
from json import JSONDecodeError


def connect_to_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        print(f'File not found: {e}')
        return '[]'
    except JSONDecodeError as e:
        print(f'JSON decode error: {e}')
        return '[]'



if __name__ == "__main__":
    json_data = connect_to_json(r'C:\Users\User\PycharmProjects\PythonHomework\data\operations.json')
    print(json_data)
