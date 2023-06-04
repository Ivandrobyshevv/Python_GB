from math import gcd


class FractionalNumber:
    def __init__(self, num: str):
        _split_digit = num.split("/")

        self.numerator = int(_split_digit[0])
        self.denominator = int(_split_digit[-1])

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if self.denominator == other.denominator:
            result = '{}/{}'.format(self.numerator + other.numerator, self.denominator)
            return FractionalNumber(result)
        cd = int(self.denominator * other.denominator / gcd(self.denominator, other.denominator))
        rn = int(cd / self.denominator * self.numerator + cd / other.denominator * self.numerator)
        g2 = gcd(rn, cd)
        numerator = int(rn / g2)
        denominator = int(cd / g2)
        result = '{}/{}'.format(numerator, denominator)
        return FractionalNumber(result)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = f"{numerator}/{denominator}"
        return FractionalNumber(result)


def multiplication(num_1: FractionalNumber, num_2: FractionalNumber) -> FractionalNumber:
    return num_1 * num_2


def addition(num_1: FractionalNumber, num_2: FractionalNumber) -> FractionalNumber:
    return num_1 + num_2


if __name__ == '__main__':
    fraction_num_1 = FractionalNumber('3/10')
    fraction_num_2 = FractionalNumber('3/5')
    result_multiplication = multiplication(fraction_num_1, fraction_num_2)
    result_addition = addition(fraction_num_1, fraction_num_2)
    print(f"FractionalNumber addition  - {fraction_num_1} + {fraction_num_2} = {result_addition}")
    print(f"FractionalNumber multiplication - {fraction_num_1} * {fraction_num_2} = {result_multiplication}")
