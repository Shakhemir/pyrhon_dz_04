"""
Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.
"""
from random import randint

file_name = 'random_numbers.txt'
numbers_count = 1000
max_number = 10000


def make_file(file):
    with open(file, 'w') as f:
        for i in range(numbers_count):
            number = randint(0, max_number)
            print(number, file=f)


def read_file_and_sort(file):
    result = []
    with open(file, 'r') as f:
        result = [int(i) for i in f.read().strip().split()]
    result.sort()
    return result


make_file(file_name)
print(*read_file_and_sort(file_name))