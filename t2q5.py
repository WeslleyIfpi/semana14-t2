def preencheLista(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(int(input()))

    return lista

def listaSemRepeticao(listaX, listaY):
    saida = []
    for i in range(len(listaX)):
        if listaX[i] not in saida:
            saida.append(listaX[i])
    for j in range(len(listaY)):
        if listaY[j] not in saida:
            saida.append(listaY[j])
            
    
    return saida

def main():
    listaX = preencheLista(10)
    listaY = preencheLista(10)

    print(listaSemRepeticao(listaX, listaY))


if __name__ == '__main__':
    main()