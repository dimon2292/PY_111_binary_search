from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать алгоритм бинарного поиска
    if not seq:
        raise ValueError
    if value not in seq:
        raise ValueError
    seq2 = seq
    while True:
        print(seq)
        index = len(seq)//2
        middle_value = seq[index]

        if middle_value == value:
            index = -1
            for i in seq2:
                index += 1
                if i == middle_value:
                    return index

        if middle_value > value:
            seq = seq[:index]
        else:
            seq = seq[index:]


#
list_ = [1,2,3,5,7,10, 12, 14, 15]
print(binary_search(14, list_))

#list2 = list_[4:]
#print(list2)