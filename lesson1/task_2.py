def is_prime(num: int) -> bool:
    return all(num % i for i in range(2, num))


def main() -> None:
    num = int(input("Введите не отрицательное число и меньше 100 000: "))
    if num < 0 or num > 100_000:
        raise ValueError(f"{num} - неверное число")
    if is_prime(num):
        print(f"{num} - простое число")
    else:
        print(f"{num} - составное число")


if __name__ == "__main__":
    main()
