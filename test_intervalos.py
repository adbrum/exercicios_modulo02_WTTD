import unittest
from intervalos import *

"""
    Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
    Exemplo:
    Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
    Saída: [100-105], [110-111], [113-115], [150]

"""

class TestIntervalo(unittest.TestCase):
    def setUp(self):
        self.enter = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
        return self.enter

    def test_intervalos(self):
        self.assertEqual(intervalos(self.setUp()), '[100-105], [110-111], [113-115], [150]')

    """
    # Primeira fase do teste.

    def test_first_slice(self):
        self.assertEqual(primeiro_intervalo(self.setUp()), '[100-105]')

    def test_second_slice(self):
        self.assertEqual(segundo_intervalo(self.setUp()), '[110-111]')

    def test_third_slice(self):
        self.assertEqual(terceiro_intervalo(self.setUp()), '[113-115]')

    def test_fourth_slice(self):
        self.assertEqual(quarto_intervalo(self.setUp()), '[115]')
    """
if __name__ == '__main__':
    unittest.main()
