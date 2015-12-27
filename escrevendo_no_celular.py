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
