from constants import LOG_DIR


def mapping(str_, data=None):
    """Возвращает по номеру колонки требуемую колонку из массива"""
    if data is None:
        data = data_()
    colomn_ = int(str_)

    return list(map(lambda row: row.split(' ')[colomn_], data))


def filter_(str_, data=None):
    """Возвращает строки по вводимому значению с этим значением"""
    if data is None:
        data = data_()

    return list(filter(lambda row: row if str_ in row else None, data))


def unique_(str_, data):
    """Возвращает массив с уникальными значениями"""
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)

    return result


def sorted_(str_, data=None):
    """Сортирует массив"""
    if data is None:
        data = data_()
    if str_ == 'asc':
        return sorted(data)
    elif str_ == 'desc':
        return sorted(data, reverse=True)


def limited_(str_, data=None):
    """Лимитирует вывод данных с массива"""
    if data is None:
        data = data_()
    value = int(str_)
    counter = 0
    result = []
    while counter < value:
        for i in data:
            result.append(i)
            counter += 1
            if counter == value:
                break

    return result


FILE_NAME = './apache_logs.txt'


def data_():
    """Формирует массив с данными"""
    with open(LOG_DIR) as f:
        data = map(lambda v: v.strip(), f)
        return list(data)

def get_query(cmd: str, str_, data=None):
    if cmd == 'filter':
        return filter_(str_=str_, data=data)
    elif cmd == 'limit':
        return limited_(str_=str_, data=data)
    elif cmd == 'map':
        return mapping(str_=str_, data=data)
    elif cmd == 'sort':
        return sorted_(str_=str_, data=data)
    elif cmd == 'unique':
        return unique_(str_=str_, data=data)
