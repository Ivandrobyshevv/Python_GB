"""
Напишите программу банкомат.
1. Начальная сумма равна нулю
2. Допустимые действия: пополнить, снять, выйти.
3. Сумма пополнения и снятия кратны 50 у.е.
4. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
5. После каждой третей операции пополнения или снятия начисляются проценты - 3%
6. Нельзя снять больше, чем на счёте
7. При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
8. Любое действие выводит сумму денег
"""

from loguru import logger

from atm_classes.atm_machine import ATMMachine

logger.remove()
logger.add("atm/logs/info.log", format="{time}|{level}|{message}", level="INFO")


def main():
    machine = ATMMachine()
    try:
        machine.start()
    except Exception as e:
        machine.stop()
        logger.error(f"Exception - {e}")


if __name__ == "__main__":
    main()
