# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def pars_path(files: list) -> None:
    for path in files:
        file_name = os.path.basename(path)
        file_ext = file_name.split('.')[-1]
        file_path = path.replace(file_name, "")
        print(file_name, file_ext, file_path, sep="\n")


def main():
    files = [
        "/Users/root1/myProject/pythonV2/lesson2/task1.py",
        "/Users/root1/myProject/pythonV2/lesson3/task2.py",
        "/Users/root1/myProject/pythonV2/lesson4/task3.py",

    ]
    pars_path(files)


if __name__ == '__main__':
    main()
