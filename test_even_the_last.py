import unittest

"""
# Melhor solução

def checkio(array):

    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

"""


def even_the_lat(array_):
    res = 0
    if array_:
        for idx, val in enumerate(array_):
            if idx % 2 == 0:
                res += val

        return res * val

    return 0


class MyTestCase(unittest.TestCase):
    def test_even_the_last01(self):
        self.assertEqual(even_the_lat([0, 1, 2, 3, 4, 5]), 30)  # "(0+2+4)*5=30"

    def test_even_the_last02(self):
        self.assertEqual(even_the_lat([1, 3, 5]), 30)  # "(1+5)*5=30"

    def test_even_the_last03(self):
        self.assertEqual(even_the_lat([6]), 36)  # "(6)*6=36"

    def test_even_the_last04(self):
        self.assertEqual(even_the_lat([]), 0)  # "An empty array = 0"


if __name__ == '__main__':
    unittest.main()

"""
Dado um vetor de números inteiros. Encontre a soma dos elementos de índices pares (0, 2, 4...)
então multiplique a soma pelo último elemento do vetor. Não se esqueça que o índice do primeiro elemento é 0.
Para um vetor vazio, o resultado será 0 (zero).
Dicas: Esta tarefa pode ser resolvida usando Índices de listas, Fatiadores and Função embutida "sum".
Input: Uma lista de inteiros.
Output: O número do tipo inteiro.
Exemplo:
checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0
1
2
3
4
5
Como é utilizado: Índices e fatias são elementos importantes para programar em python e outras linguagens.
Isto vai ser uma mão na roda.
Condições prévias: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""
