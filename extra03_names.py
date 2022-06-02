"""
Вот вам файл с английскими именами. https://cloud.mail.ru/public/J7aq/iHnLspVJR
Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это значение
на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53)
является 938-м в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?

"""


def alpha_number(name):
    result = 0
    for char in name:
        result += ord(char) - ord('A') + 1
    return result


names_file = 'english_names.txt'
with open(names_file, 'r') as f:
    names = [s.strip('"') for s in f.read().split(',')]
names.sort()
name_score = dict()
summ_of_scores = 0
for index, name in enumerate(names):
    score = (index + 1) * alpha_number(name)
    name_score[name] = score
    summ_of_scores += score
print(name_score)
print(summ_of_scores)