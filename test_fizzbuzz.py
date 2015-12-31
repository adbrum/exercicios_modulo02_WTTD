import unittest


def multiplos_de_tres(numero):
    return not numero % 3


def multiplos_de_cinco(numero):
    return not numero % 5


def fizzBuzz(numero):
    res = str(numero)

    if multiplos_de_tres(numero) and multiplos_de_cinco(numero):
        res = 'fizzbuzz'

    elif multiplos_de_tres(numero):
        res = 'fizz'

    elif multiplos_de_cinco(numero):
        res = 'buzz'

    return res


class TestFizzBuzz(unittest.TestCase):
    def test_numerosSimples(self):
        self.assertEqual(fizzBuzz(1), '1')
        self.assertEqual(fizzBuzz(2), '2')
        self.assertEqual(fizzBuzz(4), '4')

    def test_fizz(self):
        self.assertEqual(fizzBuzz(3), 'fizz')
        self.assertEqual(fizzBuzz(9), 'fizz')

    def test_buzz(self):
        self.assertEqual(fizzBuzz(5), 'buzz')
        self.assertEqual(fizzBuzz(10), 'buzz')

    def test_fizzBuzz(self):
        self.assertEqual(fizzBuzz(15), 'fizzbuzz')
        self.assertEqual(fizzBuzz(30), 'fizzbuzz')


if __name__ == '__main__':
    unittest.main()

"""
    FizzBuzz recebe um número
    FizzBuzz(1) retorna "1"
    FizzBuzz(2) retorna "2"
    FizzBuzz(3) retorna “fizz”
    FizzBuzz(9) retorna “fizz”
    FizzBuzz(4) retorna "4"
    FizzBuzz(5) retorna “buzz”
    FizzBuzz(10) retorna “buzz”
    FizzBuzz(15) retorna “fizzbuzz”
    FizzBuzz(30) retorna “fizzbuzz”
"""
