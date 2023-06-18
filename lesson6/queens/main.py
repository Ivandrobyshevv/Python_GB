import random


class App:
    def __init__(self):
        self.x = list()
        self.y = list()
        self.queen_count = 8
        self.size_board = 8
        self.correct = True

    def start(self):
        for _ in range(self.queen_count):
            new_x, new_y = [int(s) for s in input().split()]
            self.x.append(new_x)
            self.y.append(new_y)
        self.__is_beat()

    def gen_positions(self):
        result = []
        for i in range(self.size_board):
            result.append((i, random.randint(0, self.size_board - 1)))
        return result

    def __is_beat(self):
        for i in range(self.queen_count):
            for j in range(i + 1, self.queen_count):
                if self.x[i] == self.x[j] or self.y[i] == self.y[j] or (
                        abs(self.x[i] - self.x[j]) == abs(self.y[i] - self.y[j])):
                    self.correct = False
        print(self.correct)


if __name__ == "__main__":
    App().start()

