print(
"""
Написать программу, которая берет исходный список и формирует новый список. В новом списке должны содержаться все элементы из исходного, за исключением дублей.

Пример:
[1, 1, 2, 3, 5, 4, 5, 5, 6] -> [1, 2, 3, 5, 4, 6]
"""
)

lst = list(input('Введите элементы списка через пробел ').split())
print(sorted(list(set(lst))))