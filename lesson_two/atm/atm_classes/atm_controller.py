from loguru import logger

from atm_classes.atm_backend import ATMBackend


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
                case "2":
                    value = int(input("Введи сумму снятия (Сумма снятия должна быть кратна 50 у.е)\n>>> "))
                    self.__atm.withdrawals(value)
                case "3":
                    return True
                case _:
                    logger.info("Неизвестная операция")

    def accrue_interest(self) -> int:
        result = self.__atm.accrue_interest()
        return result
