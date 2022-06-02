"""
Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
"""

spisok = [1, 5, 2, 3, 4, 6, 1, 7]

def new_list(lst):
    result = [lst[0]]
    count = 0
    for i in range(1, len(lst)):
        if lst[i] > result[count]:
            result.append(lst[i])
            count += 1
    return result

new_lst = new_list(spisok)
print(new_lst)
spisok.remove(new_lst[1])
new_lst = new_list(spisok)
print(new_lst)
