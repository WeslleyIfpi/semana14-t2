def preencheLista(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(int(input()))

    return lista

def listaSemRepeticao(lista):
    saida = []
    for i in range(len(lista)):
        if lista[i] not in saida:
            saida.append(lista[i])
    
    return saida

def main():
     lista = preencheLista(20)
     print(listaSemRepeticao(lista))


if __name__ == '__main__':
    main()