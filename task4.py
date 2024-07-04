import heapq
from typing import List, Tuple


def path_find(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
    """
    Находит путь минимальной стоимости в сетке и возвращает его стоимость и путь.
    :param grid: Двумерная сетка с положительными стоимостями захода в каждую ячейку.
    :param start: Координаты начальной ячейки в виде (row, col).
    :param end: Координаты конечной ячейки в виде (row, col).
    :return: Кортеж (минимальная стоимость, список ячеек пути от начальной до конечной).
    """
    n, m = len(grid), len(grid[0])  # размеры сетки
    start_row, start_col = start

    # Массив для хранения минимальной стоимости до каждой ячейки
    cost_list = [[float('inf')] * m for _ in range(n)]
    cost_list[start_row][start_col] = grid[start_row][start_col]

    # Массив для хранения пути
    path_list = [[None] * m for _ in range(n)]

    # Очередь с приоритетами для реализации алгоритма Дейкстры
    priority_queue = [(grid[start_row][start_col], start)]
    #print(priority_queue)

    # Направления движения: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        current_cost, (current_row, current_col) = heapq.heappop(priority_queue)
        #print(priority_queue)

        # Если мы достигли конечной ячейки, можем восстановить путь
        if (current_row, current_col) == end:
            path = []
            while (current_row, current_col) is not None:
                path.append((current_row, current_col))
                if path_list[current_row][current_col] is not None:  # Проверяем, что текущая ячейка имеет предшественника
                    current_row, current_col = path_list[current_row][current_col]

                else:
                    break
            path.reverse()
            return current_cost, path # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Обход всех соседей текущей ячейки
        for drow, dcol in directions:
            new_row, new_col = current_row + drow, current_col + dcol

            # Проверка, что новый индекс находится в пределах допустимого диапазона
            if 0 <= new_row < n and 0 <= new_col < m:
                new_cost = current_cost + grid[new_row][new_col]

                # Если найден путь с меньшей стоимостью, обновляем информацию
                if new_cost < cost_list[new_row][new_col]:
                    cost_list[new_row][new_col] = new_cost
                    path_list[new_row][new_col] = (current_row, current_col)  # Обновляем путь
                    heapq.heappush(priority_queue, (new_cost, (new_row, new_col)))

    return float('inf'), []  # Если путь не найден, возвращаем бесконечность и пустой путь


if __name__ == '__main__':

    grid = [
        [1, 3, 1, 2],
        [2, 1, 3, 1],
        [3, 2, 1, 1],
        [1, 1, 1, 1]
    ]
    start = (0, 0)
    end = (3, 3)

    cost, path = path_find(grid, start, end)
    print(f"Путь: {path}")
    print(f"Минимальная стоимость: {cost}")
