import unittest

"""
# Melhor solução

def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1

"""


def index_power(array_, n):
    if not len(array_) > n >= n:
        return -1

    return pow(array_[n], n)


class MyTestCase(unittest.TestCase):
    def test_index01(self):
        self.assertEqual(index_power([1, 2, 3, 4], 2), 9)

    def test_index02(self):
        self.assertEqual(index_power([1, 3, 10, 100], 3), 1000000)

    def test_index03(self):
        self.assertEqual(index_power([0, 1], 0), 1)

    def test_index04(self):
        self.assertEqual(index_power([1, 2], 3), -1)


if __name__ == '__main__':
    unittest.main()

"""
Lhe é dado uma lista (array) com números positivos e um número N. Você deve encontrar a N-ésima potência do elemento na lista no indice N. Se N esta fora da lista, retorne -1. Não se esqueça que o primeiro elemento possui indice 0.
Vejamos alguns exemplos:
- lista = [1, 2, 3, 4] e N = 2, o resultado será 32 == 9;
- lista = [1, 2, 3] e N = 3, mas N está fora da lista, então o resultado será -1.
Entrada: Dois argumentos. Uma lista (array) de inteiros e um número como um inteiro (int).
Saida: O resultado como um inteiro (int).
Precondição: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)
"""
