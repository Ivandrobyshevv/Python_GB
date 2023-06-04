"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def get_hex(digit):
    try:
        hex_digit = hex(digit)
        return hex_digit.split("x")[1]
    except TypeError:
        raise f"Передано не целое число"


if __name__ == "__main__":
    numbers = [16, 15, 10, 100]
    numbers_hex = [(numbers[index], get_hex(numbers[index])) for index in range(len(numbers))]
    print(*numbers_hex)
