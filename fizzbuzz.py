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
