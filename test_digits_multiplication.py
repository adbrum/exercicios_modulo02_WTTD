import unittest

"""
# Melhor solução.

def multiplication(number):
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
"""


def multiplication(number):
    digit = 1
    for i in str(number):
        if int(i) == 0:
            i = 1
        digit *= int(i)
    return digit


class MyTestCase(unittest.TestCase):
    def test_2digits(self):
        self.assertEqual(multiplication(25), 10)

    def test_3digits(self):
        self.assertEqual(multiplication(125), 10)

    def test_4digits(self):
        self.assertEqual(multiplication(1253), 30)

    def test_zero(self):
        self.assertEqual(multiplication(12053), 30)

    def test_zeros(self):
        self.assertEqual(multiplication(10000), 1)

    def test_onedigit(self):
        self.assertEqual(multiplication(1), 1)


if __name__ == '__main__':
    unittest.main()

"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Example:

checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1

1
2
3
4
5
How it is used: This task can teach you how to solve a problem with simple data type conversion.

Precondition: 0 < number < 106
"""
