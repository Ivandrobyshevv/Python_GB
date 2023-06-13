"""
Напишите функцию для транспонирования матрицы
"""
import numpy as np

MATRIX = np.array(
    [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
    ])


def show_matrix(matrix) -> None:
    for _ in matrix:
        print(_)


def main():
    print("Исходная матрица:")
    show_matrix(MATRIX)
    print("Транспонированная:")
    show_matrix(MATRIX.transpose())


if __name__ == '__main__':
    main()
