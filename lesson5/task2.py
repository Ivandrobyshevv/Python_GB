# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
from typing import List

NAMES = ["Иван", "Петр", "Михаил", "Сергей"]
RATES = [10_000, 20_000, 15_000, 30_000]
PERCENTS = ["10.25%", "15.00%", "6.50%", "12.75%"]


def generate_dict(names: List[str], rates: List[int], percents: List[str]):
    yield {_[0]: _[1] * float(_[2].replace("%", "")) / 100 for _ in zip(names, rates, percents)}


def main():
    print(*generate_dict(NAMES, RATES, PERCENTS))


if __name__ == "__main__":
    main()
