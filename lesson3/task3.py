"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""
from collections import Counter


def read_document():
    with open("text.txt") as f:
        document = f.read().lower()
        return Counter(document.split(" "))


if __name__ == '__main__':
    result = read_document()
    result = {key: value for key, value in result.items() if len(key) > 2}
    for i in range(10):
        key = max(result, key=result.get)
        print(f"#{i+1} {key}:{result.pop(key)}")
