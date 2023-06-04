from typing import Tuple

from loguru import logger


class ATMBackend:
    def __init__(self):
        self.__cash = 0
        self.__percentage_for_withdrawal = 0.015
        self.__percentage_for_operations = 0.03
        self.__percentage_limit = 0.1
        self.__limit_cash = 5_000_000

    def replenish(self, value: int) -> None:
        """Зачисление средств на счет"""
        logger.info(f"Пополнение баланса на сумму: {value}у.е")
        if value_is_multiple := self.__checking_for_multiplicity(value):
            self.__cash += value
            logger.info(f"Успешное пополнение баланса. На счету: {self.__cash}у.е")
            print(f"Баланс {self.__cash}")

    def withdrawals(self, value: int):
        """Списание денежных средств"""
        logger.info(f"Снятие средств: {value}")
        value_is_multiple = self.__checking_for_multiplicity(value)
        value_lt_cash, percentage = self.__checking_lt_cash(value)
        if all((value_lt_cash, value_is_multiple)):
            self.__cash -= value + percentage
            logger.info(f"Успешное списание. На счету: {self.__cash}у.е")
            print(f"Баланс {self.__cash}")

    def __get_percentage_for_withdrawal(self, value: int) -> int:
        logger.info(f"Расчет комиссии за списание денежных средств")
        max_amount = 600
        min_amount = 30
        amount = int(value * self.__percentage_for_withdrawal)
        if amount < min_amount:
            logger.info(f"Комиссия составляет {min_amount}у.е")
            print(f"Комиссия составляет {min_amount}у.е")
            return min_amount
        if amount > max_amount:
            logger.info(f"Комиссия составляет {max_amount}у.е")
            print(f"Комиссия составляет {max_amount}у.е")
            return max_amount
        logger.info(f"Комиссия составляет {amount}у.е")
        print(f"Комиссия составляет {amount}у.е")
        return amount

    def __checking_for_multiplicity(self, value: int) -> bool:
        """
        Проверка на кратность 50
        :param value: значения для пополнения/списания
        :return: Ture - Соответствует условию. False - не соответствует.
        """
        if value < 0:
            print(f"Не корректное значение {value}")
            return False
        if value % 50 == 0:
            return True
        logger.info(f"Значение не кратно 50. На счету: {self.__cash}у.е")
        print("Значение не кратно 50!")
        print(f"Баланс {self.__cash}")
        return False

    def __checking_lt_cash(self, value: int) -> Tuple[bool, int]:
        percentage = self.__get_percentage_for_withdrawal(value)
        if (self.__cash - value - percentage) > 0:
            return True, percentage
        print(f"Недостаточно средств для списания. Баланс: {self.__cash}")
        return False, percentage

    def limit_cash(self):
        """Проверка на превышении лимита"""
        if self.__cash > self.__limit_cash:
            print(f"Превышен лимит на балансе - {self.__cash}")
            print(f"Каждая операция списывает {self.__percentage_limit * 100}%")
            self.__cash -= self.__cash * self.__percentage_limit

    def accrue_interest(self):
        self.__cash += int(self.__cash * self.__percentage_for_operations)
        return self.__cash
