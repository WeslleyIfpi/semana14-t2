def preencheLista(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(int(input()))

    return lista

def contaNegativos(lista):
    negativos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos += 1
    
    return negativos

def somaPositivos(lista):
    somatorio = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            somatorio += lista[i]

    return somatorio

def main():
    lista = preencheLista(10)
    print(lista)
    print(contaNegativos(lista))
    print(somaPositivos(lista))


if __name__ == '__main__':
    main()