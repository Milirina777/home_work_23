from constants import LOG_DIR


def mapping(str_, data=None):
    """Возвращает по номеру колонки требуемую колонку из массива"""
    if data is None:
        data = data_base()
    colomn_ = int(str_)

    return list(map(lambda row: row.split(' ')[colomn_], data))


def filter_data(str_, data=None):
    """Возвращает строки по вводимому значению с этим значением"""
    if data is None:
        data = data_base()

    return list(filter(lambda row: row if str_ in row else None, data))


def unique_data(str_, data):
    """Возвращает массив с уникальными значениями"""
    return list(set(data))


def sorted_data(str_, data=None):
    """Сортирует массив"""
    if data is None:
        data = data_base()
    if str_ == 'desc':
        return sorted(data, reverse=True)
    return sorted(data)


def limited_data(str_, data=None):
    """Лимитирует вывод данных с массива"""
    if data is None:
        data = data_base()
    value = int(str_)

    return data[: int(value)]


FILE_NAME = './apache_logs.txt'


def data_base():
    """Формирует массив с данными"""
    with open(LOG_DIR) as f:
        data = map(lambda v: v.strip(), f)
        return list(data)

def get_query(cmd: str, str_, data=None):
    if cmd == 'filter':
        return filter_data(str_=str_, data=data)
    elif cmd == 'limit':
        return limited_data(str_=str_, data=data)
    elif cmd == 'map':
        return mapping(str_=str_, data=data)
    elif cmd == 'sort':
        return sorted_data(str_=str_, data=data)
    elif cmd == 'unique':
        return unique_data(str_=str_, data=data)
