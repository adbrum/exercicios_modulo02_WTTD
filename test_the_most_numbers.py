import unittest

"""
# Melhor solução

def checkio(*args):
    return max(args) - min(args) if args else 0

"""


def the_most_number(*args):
    if args:
        return max(args) - min(args)

    return 0


def almost_equal(checked, correct, significant_digits):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


class MyTestCase(unittest.TestCase):
    def test_the_most_number01(self):
        self.assertEquals(almost_equal(the_most_number(1, 2, 3), 2, 3), True)  # "3-1=2"

    def test_the_most_number02(self):
        self.assertEqual(almost_equal(the_most_number(5, -5), 10, 3), True)  # "5-(-5)=10"

    def test_the_most_number03(self):
        self.assertEqual(almost_equal(the_most_number(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), True)  # "10.2-(-2.2)=12.4"

    def test_the_most_number_empty(self):
        self.assertEqual(almost_equal(the_most_number(), 0, 3), True)  # "Empty"


if __name__ == '__main__':
    unittest.main()

"""
Let's work with numbers.

You are given an array of numbers (floats). You should find the difference between the maximum and minimum element.
Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function
should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions (read about this here).
So we should check the result with ±0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between maximum and minimum as a number (int, float).

Example:

checkio(1, 2, 3) == 2
checkio(5, -5) == 10
checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
checkio() == 0

1
2
3
4
5
How it is used: Here you will learn about passing an undefined amount of arguments to functions.

Precondition: 0 ≤ len(args) ≤ 20
all(-100 < x < 100 for x in args)
all(isinstance(x, (int, float)) for x in args)
"""
