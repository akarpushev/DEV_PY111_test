import random


def counting_sort(arr):
    # Диапазон значений
    min_value = 13
    max_value = 25

    # Массив счетчиков с размерами на основе диапазона 25-13+1=13
    count = [0] * (max_value - min_value + 1)
    #print(count)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Подсчет количества каждого значения в массиве
    for num in arr:
        count[num - min_value] += 1
    #print(count)

    # Результатирующий массив
    sorted_arr = []

    # Проход по массиву счетчиков и восстанавление отсортированного массива
    for i in range(len(count)):
        sorted_arr.extend([i + min_value] * count[i])
        #print(sorted_arr)

    return sorted_arr


if __name__ == '__main__':

    # Массив из 10^6 элементов в диапазоне от 13 до 25
    array = [random.randint(13, 25) for _ in range(10 ** 6)]

    sorted_array = counting_sort(array)

    # Проверка: вывод первых 20 элементов для демонстрации
    print(sorted_array[:20])
    # Проверка правильности сортировки
    assert sorted_array == sorted(array), "Массив отсортирован неправильно!"
