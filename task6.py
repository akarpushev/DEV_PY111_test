from typing import List, Tuple


def rent_rockets(requests: List[Tuple[int, int]]) -> str:
    """
    Проверить, можно ли удовлетворить все заявки на аренду одной ракетой.
    :param requests: Список заявок на аренду ракет в виде (час_начала, час_конца)
    :return: Хватит, если одной ракеты достаточно, иначе не хватит
    """
    # Список событий (время, тип события), где тип события: 1 - начало аренды, -1 - конец аренды
    events = []
    for start, end in requests:
        events.append((start, 1))  # начало аренды
        events.append((end, -1))  # конец аренды
        #print(events)

    # Сортировка событий. При равенстве времени сначала обрабатываем завершения аренды (приоритет -1)
    # Сначала сортируем по времени - x[0], потом по событию
    events.sort(key=lambda x: (x[0], x[1]))
    #print(events)

    current_rent = 0  # текущее количество арендованных ракет

    for event in events:
        # распаковка кортежа на отдельные составляющие
        time, event_type = event
        #print(time, event_type)
        #print(event)
        current_rent += event_type
        #print(current_rent)
        # Если в какой-то момент требуется больше одной ракеты
        if current_rent > 1:
            return "Oдной ракеты не хватит"

    # Если current_rent никогда не превышает одну ракету
    return "Oдной ракеты хватит"


if __name__ == '__main__':

    requests = [(1, 4), (2, 3), (3, 5), (7, 8)]
    print(rent_rockets(requests))  # Вывод: Одной ракеты не хватит

    requests = [(1, 2), (2, 3), (3, 4), (4, 5)]
    print(rent_rockets(requests))  # Вывод: Одной ракеты хватит
