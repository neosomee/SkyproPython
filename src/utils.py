import json
from json import JSONDecodeError
import logging
import os

logger = logging.getLogger(__name__)
log_dir = '../logs'


file_handler = logging.FileHandler(os.path.join(log_dir, 'utils.log'))
file_formater = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# Логирование сообщений
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical("Critical message")


def connect_to_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug(f'Successfully loaded JSON data from {path}')
            return data
    except FileNotFoundError as e:
        logger.error(f'File not found: {e}')
        print(f'File not found: {e}')
        return '[]'
    except JSONDecodeError as e:
        logger.error(f'JSON decode error: {e}')
        print(f'JSON decode error: {e}')
        return '[]'



if __name__ == "__main__":
    json_data = connect_to_json(r'C:\Users\User\PycharmProjects\PythonHomework\data\operations.json')
    print(json_data)
