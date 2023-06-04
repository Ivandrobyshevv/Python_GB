"""
Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""
from collections import Counter


def main(elements):
    frequencies = Counter(elements)
    result = [key for key, value in frequencies.items() if value > 1]
    print(result)


if __name__ == '__main__':
    main([1, 2, 3, 1, 2, 3, 4, 5, 2, 1, 10, 100])
