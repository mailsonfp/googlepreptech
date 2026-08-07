def fibbonaci(n):
    retorno = [0] * 31

    retorno[0] = 0
    retorno[1] = 1

    for i in range(2, 31):
        retorno[i] = retorno[i - 2] + retorno[i - 1]

    return retorno[n]


if __name__ == '__main__':
    print(fibbonaci(10))
