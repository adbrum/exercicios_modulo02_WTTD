import unittest

"""
# Melhor soluão.

def three_words(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False

"""


def three_words(words):
    count = 0
    for word in words.split(' '):
        count += 1
        if word.isdigit():
            count = 0
        if count == 3:
            return True

    return False


class MyTestCase(unittest.TestCase):
    def test_three_words01(self):
        self.assertEqual(three_words("Hello World hello"), True)

    def test_three_words02(self):
        self.assertEqual(three_words("He is 123 man"), False)

    def test_three_words03(self):
        self.assertEqual(three_words("bla bla bla bla"), True)

    def test_three_words04(self):
        self.assertEqual(three_words("Hi"), False)

    def test_three_words05(self):
        self.assertEqual(three_words("start 5 one two three 7 end"), True)


if __name__ == '__main__':
    unittest.main()

"""
Vamos ensinar os Robôs a distinguir palavras e números.

Lhe é dada uma string com palavras e números separados por espaços em branco (um espaço).
As palavras contêm apenas letras. Você deve verificar se a string contém três palavras em sucessão.
Por exemplo, a string "start 5 one two three 7 end" contém três palavras em sucessão.

Entrada: Uma string com palavras.

Saída: A resposta como boolean.

Exemplo:

checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False

1
2
3
4
5
6
Onde é usado: Isto lhe ensina a trabalhar com srings e introduz algumas funções muito úteis.

Precondições: A entrada contém palavras e/ou números. Não existem palavras misturadas (letras e números juntos).
0 < len(words) < 100
"""
