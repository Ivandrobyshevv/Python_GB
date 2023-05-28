class Triangle:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    def show_triangle_info(self) -> None:
        if self.is_triangle():
            if self.__a == self.__b and self.__a == self.__c and self.__b == self.__c:
                print("Равносторонний треугольник")
            elif self.__a != self.__b and self.__a != self.__c and self.__b != self.__c:
                print('Разносторонний треугольник')
            else:
                print('Равнобедренный треугольник')
        else:
            print("Треугольник не существует")

    def is_triangle(self) -> bool:
        if (self.__a + self.__b) > self.__c and (self.__a + self.__c) > self.__b and (self.__c + self.__b) > self.__a:
            return True
        return False

    @staticmethod
    def __print_result(message: str) -> None:
        print(message)


def main() -> None:
    try:
        a, b, c = map(int, input("Введите стороны треугольника [a,b,c]: ").split(","))
        triangle = Triangle(a, b, c)
        triangle.show_triangle_info()
    except ValueError:
        raise ValueError("Введите корректные данные")


if __name__ == '__main__':
    main()
