def indice(intervalo, a, b):
    return '[' + str(intervalo[a]) + '-' + str(intervalo[b]) + ']'


def intervalos(intervalo):
    for i in intervalo:
        if i == intervalo[0]:
            a = indice(intervalo, 0, 5)
        if i == intervalo[6]:
            b = indice(intervalo, 6, 7)
        if i == intervalo[8]:
            c = indice(intervalo, 8, 10)
        if i == intervalo[-1]:
            d = ('[' + str(intervalo[-1]) + ']')

    conjunto = '{0}, {1}, {2}, {3}'.format(a, b, c, d)

    return conjunto


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
