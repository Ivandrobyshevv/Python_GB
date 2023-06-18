from datetime import datetime
from sys import argv


class CheckData:

    def check(self) -> str:
        if len(argv) == 2:
            _, dt = argv
            return self.__checker(dt)
        return "Date is None"

    def __checker(self, dt: str) -> str:
        if self.__date_validator(dt):
            return "Date is valid"
        return "Invalid date"

    @staticmethod
    def __date_validator(dt: str) -> bool:
        try:
            datetime.strptime(dt, "%d.%m.%Y").date()
            return True
        except:
            return False


if __name__ == '__main__':
    res = CheckData().check()
    print(res)
