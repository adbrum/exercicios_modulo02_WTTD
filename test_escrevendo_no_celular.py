import unittest


def digits():
    digit = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}

    return digit


def position(set, word):
    count = 0
    for i in set:
        count += 1
        if i == word:
            return count


def validate(phrase):
    result = ''
    digit = digits()  # recebe o dicionario
    for char in phrase:  # pega cada letra da phrase
        for key, value in digit.items():  # pega chave e valor dos item do dicionário
            for val in value:  # pega cada letra do valor
                if val == char:  # se o valor for igual a letra
                    pos = position(digit[key], char)  # recebe a posição da letra no conjunto
                    result += (str(key) * pos)  # multiplica a str(chave) pelo nº da posição

    return result


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.phrase = 'WELCOME TO THE DJANGO'

    def test_position(self):
        self.assertEqual(position('PQRS', 'S'), 4)
        self.assertEqual(position('PQRS', 'R'), 3)
        self.assertEqual(position('PQRS', 'P'), 1)

    def test_validate(self):
        self.assertEqual(validate(self.phrase), '933555222666633086660844330352664666')


if __name__ == '__main__':
    unittest.main()

"""
Um dos serviços mais utilizados pelos usuários de aparelhos celulares são os SMS (Short Message Service), que permite o envio de mensagens curtas (até 255 caracteres em redes GSM e 160 caracteres em redes CDMA).
Para digitar uma mensagem em um aparelho que não possui um teclado QWERTY embutido é necessário fazer algumas combinações das 10 teclas numéricas do aparelho para conseguir digitar. Cada número é associado a um conjunto de letras como a seguir:
Letras  ->  Número
ABC    ->  2
DEF    ->  3
GHI    ->  4
JKL    ->  5
MNO    ->  6
PQRS    ->  7
TUV    ->  8
WXYZ   ->  9
Espaço -> 0
Desenvolva um programa que, dada uma mensagem de texto limitada a 255 caracteres, retorne a seqüência de números que precisa ser digitada. Uma pausa, para ser possível obter duas letras referenciadas pelo mesmo número, deve ser indicada como _.
Por exemplo, para digitar "SEMPRE ACESSO O DOJOPUZZLES", você precisa digitar:
7777336777733022223377777777666066603666566678899999999555337777
"""

"""
# Segunda fase dos testes

def test_position_word(self):
    self.assertEqual(repeats_amount_of_letter('PQRS', 'S'), 'SSSS')
    self.assertEqual(repeats_amount_of_letter('PQRS', 'R'), 'RRR')
    self.assertEqual(repeats_amount_of_letter('PQRS', 'P'), 'P')
"""

"""
# Segunda fase dos testes

def repeats_amount_of_letter(set, word):
count = 0
for i in set:
    count += 1
    if i == word:

        return (word *count)
"""

"""
# Primeira fase dos testes.

def digito2(digito):
return 'ABC'


def digito3(digito):
return 'DEF'


def digito4(digito):
return 'GHI'


def digito5(digito):
return 'JKL'


def digito6(digito):
return 'MNO'


def digito7(digito):
return 'PQRS'


def digito8(digito):
return 'TUV'


def digito9(digito):
return 'WXYZ'


def digito0(digito):
return ' '

"""

"""
# Primeira fase dos testes.

def test_digito2(self):
    self.assertEqual(digito2(2), 'ABC')

def test_digito3(self):
    self.assertEqual(digito3(3), 'DEF')

def test_digito4(self):
    self.assertEqual(digito4(4), 'GHI')

def test_digito5(self):
    self.assertEqual(digito5(5), 'JKL')

def test_digito6(self):
    self.assertEqual(digito6(6), 'MNO')

def test_digito7(self):
    self.assertEqual(digito7(7), 'PQRS')

def test_digito8(self):
    self.assertEqual(digito8(8), 'TUV')

def test_digito9(self):
    self.assertEqual(digito9(9), 'WXYZ')

def test_digito0(self):
    self.assertEqual(digito0(0), ' ')
"""
