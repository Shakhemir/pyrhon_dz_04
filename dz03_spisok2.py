"""
Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
и содержащие максимальное количество элементов.
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
 [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
"""


def new_list(lst):
    result = [lst[0]]
    count = 0
    next_count = 0
    is_next = False
    for i in range(1, len(lst)):
        if lst[i] > result[count]:
            result.append(lst[i])
            count += 1
        elif not is_next:
            next_count = i
            is_next = True
    return result, next_count


def list_of_lists(lst):
    result = []
    next = 1
    while next > 0:
        new_lst, next = new_list(lst)
        result.append(new_lst)
        lst.pop(next - 1)
    return result


def max_list(spisok):
    lists = list_of_lists(spisok)
    max_len = len(lists[0])
    for i, lst in enumerate(lists):
        if len(lst) > max_len:
            max_len = len(lst)
            result = lst
    return result


print(__doc__)
# spisok = [1, 5, 2, 3, 4, 6, 1, 7]
spisok = [5, 2, 3, 4, 6, 1, 7]
print(max_list(spisok))
