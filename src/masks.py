import logging
import os
logger = logging.getLogger(__name__)
log_dir = '../logs'


file_handler = logging.FileHandler(os.path.join(log_dir, 'masks.log'))
file_formater = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# Логирование сообщений
logger.debug('Debug message')
logger.info('Info message')


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, показывая первые 6 и последние 4 цифры,
    а остальные заменяет на символы '*'.
    """
    logger.debug('Succesfully mask first 6 numbers')
    return f"{card_number[:6]} {'*' * 6} {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, отображая только последние 4 цифры,
    предшествующие которым ставятся два символа '*'.
    """
    logger.info('Succesfully mask last 4 numbers')
    return f"**{account_number[-4:]}"
