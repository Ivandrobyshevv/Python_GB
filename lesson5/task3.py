# Генератор чисел Фибоначчи

FIB_SET = (5, 8, 10, 15)


def generate_fib(num: int):
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(num):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def main():
    for n in FIB_SET:
        print(*generate_fib(n))


if __name__ == "__main__":
    main()
