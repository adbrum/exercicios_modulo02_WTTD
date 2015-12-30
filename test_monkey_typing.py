import unittest

"""
# Melhor solução

def count_words(text, words):
    return sum(w in text.lower() for w in words)

"""


def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1

    return count


class MyTestCase(unittest.TestCase):
    def test_count_words01(self):
        self.assertEqual(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}), 3)

    def test_count_words02(self):
        self.assertEqual(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}), 2)

    def test_count_words03(self):
        self.assertEqual(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                                     {"sum", "hamlet", "infinity", "anything"}), 1)


if __name__ == '__main__':
    unittest.main()

"""
... Se eu deixar meus dedos passearem ociosamente sobre as teclas de uma máquina de escrever,
pode acontecer que a minha fita fez uma frase inteligível. Se um exército de macacos forem dedilhando em
máquinas de escrever eles podem vir a escrever todos os livros do Museu Britânico. A chance de isto acontecer é
decididamente mais favoráveis do que a chance de as moléculas retornarem a metade da embarcação.
A. S. Eddington. The Nature of the Physical World: The Gifford Lectures, 1927.
"Ford!" disse ele, "há um número infinito de macacos lá fora que querem conversar conosco sobre esse script para
Hamlet que eles criaram."
Douglas Adams. O Guia do Mochileiro das Galáxias.
O Teorema do macaco infinito afirma que um macaco digitando aleatoriamente em um teclado por um intervalo de tempo
infinito irá certamente criar um texto qualquer escolhido, como por exemplo a obra completa de John Wallis,
ou mais provavelmente, um livro de Dan Brown.

Vamos supor que os nossos macacos estão escrevendo, escrevendo e escrevendo, e produziram uma grande variedade de
pequenos segmentos de texto. Vamos tentar verificá-los para inclusões de algumas palavras que sejam sensatas.

Lhe é dado algum texto que potencialmente inclui algumas palavras sensatas. Você deve contar quantas palavras estão
incluídas no texto dado. Uma palavra deve ser completa e pode ser uma parte de outra palavra. As palavras são dadas
em letras minúsculas e não repetem. Se uma palavra aparece várias vezes no texto, esta deve ser contada apenas uma vez.

Por Exemplo, texto - "How aresjfhdskfhskd you?", palavras - ("how", "are", "you", "hello"). O resultado seria 3.

Entrada: Dois argumentos. Um texto como uma string (unicode para py2) e palavras como um set de strings (unicode para py2).

Saída: O número de palavras no texto como um inteiro.

Exemplo:

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1

1
2
3
4
5
Como é utilizado: Python é uma linguagem muito util e poderosa para processamento de texto. Está missão é apenas um exemplo simples to tipo de ferramenta de busca de texto que você pode construir.

pré-condição:
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
"""
