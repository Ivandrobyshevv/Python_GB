"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
"""
from itertools import combinations
from typing import Dict, List, Iterator

THINGS = {
    "bag": 10,
    "vest": 10,
    "sweatshirt": 5,
    "camisole": 5,
    "shirt": 3,
    "dress": 3,
    'jeans': 2,
    'water': 1
}


class BagPack:
    def __init__(self, things: Dict[str, int], bag_volume: int) -> None:
        self.things = things
        self.bag_volume = bag_volume
        self.__remainder = bag_volume

    def build(self) -> None:
        """Сборка рюкзака"""
        tmp = 0
        for thing, weight in self.__packing_things():
            if (tmp + weight) <= self.bag_volume:
                tmp += weight
                self.__show_bag(thing, weight)

    def __show_bag(self, thing: str, weight: int) -> None:
        """
        Выводим в консоль полученные значения
        :param thing: Название вещи
        :param weight: Вес вещи
        """
        self.__remainder -= weight
        print(f"Берем: {thing}. Вес: {weight}. Осталось места: {self.__remainder}")

    def __packing_things(self) -> Iterator[str | int]:
        """Сортируем словарь по массе"""
        for thing, weight in sorted(self.things.items(), key=lambda x: x[1]):
            yield thing, weight


if __name__ == "__main__":
    bag = BagPack(THINGS, 10)
    bag.build()
