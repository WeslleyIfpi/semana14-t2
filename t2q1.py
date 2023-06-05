def preencheLista(quantidade):
    lista = []
    for i in range(quantidade):
        lista.append(int(input()))

    return lista


def main():
    lista =  preencheLista(10)

    print(lista)
    print(max(lista))
    print(lista.index(max(lista)))


if __name__ == '__main__':
    main()