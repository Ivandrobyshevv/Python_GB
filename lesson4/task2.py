"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""


def render_dict(**kwargs):
    result = dict()
    for k, v in kwargs.items():
        if v.__hash__ is not None:
            result[v] = k
        else:
            result[f'{v}'] = k
    return result


def main():
    print("Исх. параметры: first='one', second=2, third=3, fourth='four', fifth=[2, 3]")
    print(render_dict(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))


if __name__ == "__main__":
    main()
