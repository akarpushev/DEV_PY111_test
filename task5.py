from collections import Counter
from typing import List


def consensus_string(sequences: List[str]) -> str:
    """
    Строит консенсус-строку из списка DNA последовательностей.
    :param sequences: Список строк с DNA последовательностями одинаковой длины
    :return: Консенсус-строка
    """
    if not sequences:
        return ""

    # Длина каждой строки
    length = len(sequences[0])

    # Консенсус-строка
    consensus = []

    # Проход по каждой позиции в строках
    for i in range(length):
        # Сбор всех символов для текущей позиции из всех строк
        column_letters = [letter[i] for letter in sequences]
        #print(column_letters)

        # Counter, чтобы найти наиболее частый символ
        most_common_letter, _ = Counter(column_letters).most_common(1)[0]
        #print(most_common_letter)

        # Добавка наиболее частого символа в консенсус-строку
        consensus.append(most_common_letter)

    # Преобразование списка символов в строку
    return ''.join(consensus)


if __name__ == '__main__':

    dna_sequences = [
        "ATTA",
        "ACTA",
        "AGCA",
        "ACAA"
    ]

    consensus = consensus_string(dna_sequences)
    print("Консенсус-строка:", consensus)  # Вывод: Консенсус-строка: ACTA
