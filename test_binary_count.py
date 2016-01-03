import unittest

"""
# Outra solução.

binary_count=lambda n:bin(n).count('1')

"""


def binary_count(number):
    return bin(number)[2:].count('1')


class MyTestCase(unittest.TestCase):
    def test_binary_count01(self):
        self.assertEqual(binary_count(4), 1)

    def test_binary_count02(self):
        self.assertEqual(binary_count(15), 4)

    def test_binary_count03(self):
        self.assertEqual(binary_count(1), 1)

    def test_binary_count04(self):
        self.assertEqual(binary_count(1022), 9)


if __name__ == '__main__':
    unittest.main()

"""
For the Robots the decimal format is inconvenient. If they need to count to "1", their computer brains want to count it
in the binary representation of that number. You can read more about binary here.

You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1)
are in the number spelling. For example: 5 = 0b101 contains two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.

Example:

checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9

1
2
3
4
5
How it is used: How to convert a number to the binary form. It can be useful for Computer Science purposes.

Precondition: 0 < number ≤ 232
"""
