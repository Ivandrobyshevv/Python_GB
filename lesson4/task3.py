"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""
import datetime

from loguru import logger

from lesson2.atm.atm_classes.atm_backend import ATMBackend

TRANSACTION = []

now = datetime.datetime.now()


class ATMMachineController:
    def __init__(self):
        self.__atm = ATMBackend()
        self.__count_operations = 1

    def __call__(self):
        print("Банк Комиссионный")
        while True:
            action = input("1 - Пополнить\n2 - Снятия\n3 - Выйти\n>> ")
            self.__atm.limit_cash()
            if self.__count_operations % 3 == 0:
                print("Начисление процентов: 3%")
                cash = self.__atm.accrue_interest()
                print(f"Баланс: {cash}у.е")
            self.__count_operations += 1
            match action:
                case "1":
                    value = int(input("Введи сумму пополнение (Сумма пополнения должна быть кратна 50 у.е)\n>>> "))
                    self.__atm.replenish(value)
                    TRANSACTION.append(f'datatime: {now} | Зачисление')
                case "2":
                    value = int(input("Введи сумму снятия (Сумма снятия должна быть кратна 50 у.е)\n>>> "))
                    self.__atm.withdrawals(value)
                    TRANSACTION.append(f'datatime: {now} | Списание')
                case "3":
                    print(*TRANSACTION)
                    return True
                case _:
                    logger.info("Неизвестная операция")

    def accrue_interest(self) -> int:
        result = self.__atm.accrue_interest()
        return result


class ATMMachine:
    def __init__(self):
        self.__stop = True
        self.__controller = ATMMachineController()
        self.__count_operation = 0

    def start(self):
        while self.__stop:
            if self.__controller():
                self.stop()

    def stop(self):
        self.__stop = False
        print(f"Выход")


if __name__ == "__main__":
    ATMMachine().start()
