def last_person_number(n: int, k: int) -> int:
    """
    Возвращает позицию последнего оставшегося человека в игре по считалочке с N людьми и считалкой из K слогов.
    :param n: Общее количество человек
    :param k: Количество слогов в считалочке
    :return: Позиция последнего оставшегося человека (нумерация с 1)
    """
    position = 0
    for i in range(2, n + 1):
        position = (position + k) % i
    return position + 1


if __name__ == '__main__':
    print(last_person_number(7, 3))
