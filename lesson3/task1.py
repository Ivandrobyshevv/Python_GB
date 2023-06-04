"""
Task 1
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.

*Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.

Task 2
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях

Task 3
Создайте вручную кортеж содержащий элементы разных типов.

Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа

Task 4
Создайте вручную список с повторяющимися элементами.

Удалите из него все элементы, которые встречаются дважды.


Task 5
Создайте вручную список с повторяющимися целыми числами.

Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
Нумерация начинается с единицы.
"""
from collections import Counter

numbers = [1, 1, 2, 3, 4, 4, 5]


def get_unique_numbers():
    unique_numbers = []
    for number in numbers:
        if number in unique_numbers:
            continue
        unique_numbers.append(number)
    return unique_numbers


def task1():
    print("Задание 1")
    unique_numbers = list(set(numbers))
    print(f"Короткое - {unique_numbers}")
    unique_numbers = get_unique_numbers()
    print(f"Длинное - {unique_numbers}")


def task2(value):
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float):
        return float(value)
    if any(filter(lambda x: x.isupper(), value)):
        return value.lower()
    return value.lower()


def show_task2():
    print("Задание 2")
    print(f"Целое положительное число - {task2(100)}")
    print(f"Вещественное положительное - {task2(5.5)}")
    print(f"Вещественное отрицательное - {task2(-5.5)}")
    print(f"Строку в нижнем регистре - {task2('sdasdaAA')}")
    print(f"В остальных случаях - {task2('sdasda')}")


def task3():
    print("Задание 3")
    elements = ("dass", "1", 1, 2.3, 2, 12, 10, 100.1, "100,1")
    elements_dict = dict()
    for element in elements:
        if elements_dict.get(f"{type(element)}") is None:
            elements_dict[f"{type(element)}"] = [element]
            continue
        elements_dict[f"{type(element)}"].append(element)
    print(elements_dict)


def task4(data):
    print("Задание 4")
    frequencies = Counter(data)
    filtered = [i for i in data if frequencies.get(i) != 2]
    print(filtered)


def task5(data):
    print("Задание 5")
    result = [i for i in range(1, len(data), 2)]
    print(result)


if __name__ == '__main__':
    task1()
    print()
    show_task2()
    print()
    task3()
    print()
    task4(['adad', "adad", "1", 2, "1", 3, 4, 1])
    print()
    task5(['adad', "adad", "1", 2, "1", 3, 4, 1])
