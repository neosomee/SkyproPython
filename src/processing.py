def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.
    Возвращает новый список словарей с указанным состоянием.
    """
    filtered_data = []
    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(data, descending=True):
    """
    Сортирует список словарей по дате.
    Возвращает новый отсортированный список.
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
