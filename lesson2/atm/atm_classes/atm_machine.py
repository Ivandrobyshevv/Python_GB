from loguru import logger

from atm_classes.atm_controller import ATMMachineController


class ATMMachine:
    def __init__(self):
        self.__stop = True
        self.__controller = ATMMachineController()
        self.__count_operation = 0

    def start(self):
        logger.info("Starting ATMMachine")
        while self.__stop:
            if self.__controller():
                self.stop()

    def stop(self):
        self.__stop = False
        print(f"Выход")
        logger.info("Stopping ATMMachine")
