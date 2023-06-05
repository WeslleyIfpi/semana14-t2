def preencheLista(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(int(input()))

    return lista

def produtoEscalar(listaX, listaY):
    total = 0
    for i in range(len(listaX)):
        total += listaX[i] * listaY[i]

    return total

def montaSaida(listaX, listaY):
    saida = ''
    for i in range(len(listaX)):
        saida += f'({listaX[i]} x {listaY[i]})'
        if i+1 != len(listaX):
            saida += ' + '
        else:
            saida += ' = '
    
    return saida

def main():
    listaX = preencheLista(5)
    listaY = preencheLista(5)

    print(listaX)
    print(listaY)
    print(f"{montaSaida(listaX, listaY)}{produtoEscalar(listaX, listaY)}")



if __name__ == '__main__':
    main()