from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def program():
    count = 1
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    while True:
        if count > 11:
            print(f"Попыткой закончились, загаданное число: {num}")
            break
        guess = int(input("Угадай число: "))
        if guess < num:
            print(f"Попыткой использовано {count}")
            print("Больше")
        elif guess > num:
            print(f"Попыткой использовано {count}")
            print("Меньше")
        elif guess == num:
            print(f"Попыткой использовано {count}")
            print("Ты угадал!")
            break
        count += 1


if __name__ == "__main__":
    program()
