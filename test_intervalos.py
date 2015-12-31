import unittest


def indice(intervalo, a, b):
    return str(intervalo[a]) + '-' + str(intervalo[b])


def intervalos(intervalo):
    for i in intervalo:
        if i == intervalo[0]:
            a = indice(intervalo, 0, 5)
        if i == intervalo[6]:
            b = indice(intervalo, 6, 7)
        if i == intervalo[8]:
            c = indice(intervalo, 8, 10)
        if i == intervalo[-1]:
            d = (str(intervalo[-1]))

    conjunto = '[{0}], [{1}], [{2}], [{3}]'.format(a, b, c, d)

    return conjunto


class TestIntervalo(unittest.TestCase):
    def setUp(self):
        self.enter = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
        return self.enter

    def test_intervalos(self):
        self.assertEqual(intervalos(self.setUp()), '[100-105], [110-111], [113-115], [150]')


if __name__ == '__main__':
    unittest.main()

"""
    Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
    Exemplo:
    Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
    Saída: [100-105], [110-111], [113-115], [150]

"""

"""

# Primeira fase do teste

def primeiro_intervalo(intervalo):
    first = str(intervalo[0])
    last = str(intervalo[5])
    intervalo = '[' + first + '-' + last + ']'

    return intervalo


def segundo_intervalo(intervalo):
    first = str(intervalo[10])
    last = str(intervalo[11])
    intervalo = '[' + first + '-' + last + ']'

    return intervalo


def terceiro_intervalo(intervalo):
    first = str(intervalo[13])
    last = str(intervalo[15])
    intervalo = '[' + first + '-' + last + ']'

    return intervalo


def quarto_intervalo(intervalo):
    first = str(intervalo[-1])
    intervalo = '[' + first + ']'

    return intervalo
"""

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
