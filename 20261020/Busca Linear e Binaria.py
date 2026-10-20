def linear(lista, n):
    # for elemento in lista:
    #     if elemento == n:
    #         return lista.index(elemento)
    # return -1

    for i in range(len(lista)):
        if lista[i] == n:
            return i
    return -1



def binaria(lista, n):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == n:
            return meio
        elif n < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

if __name__ == '__main__':
    # print(linear([12, 10, 20, 15, 30], 50))
    # print(linear([12, 10, 20, 15, 30], 15))
    #
    # #pre requisito a lista precisa estar ordenada senao ele nao acha
    # print(binaria([10, 12, 15, 20, 30], 50))
    # print(binaria([10, 12, 15, 18, 20, 25, 30, 50, 79, 90], 50))
    # print(binaria([10, 12, 15, 18, 20, 25, 30, 50, 79, 90], 12))
    # print('Ele NAO ACHA SE NAO ESTIVER ORDENADO')
    # print(binaria([10, 12, 50, 18, 20, 25, 30, 60, 79, 90], 50))
    #
    # print('Medindo o tempo')
    # from datetime  import datetime
    # numeros = list(range(50000000))
    #
    # inicio = datetime.now()
    # print(linear(numeros, -90))
    # fim = datetime.now()
    # print(f'Tempo busca linear: {fim - inicio}')
    #
    # inicio = datetime.now()
    # print(binaria(numeros, -90))
    # fim = datetime.now()
    # print(f'Tempo busca binaria: {fim - inicio}')

    print('Medindo o tempo preciso')
    import time
    numeros = list(range(50000000))

    inicio = time.perf_counter()
    print(linear(numeros, -90))
    fim = time.perf_counter()
    print(f'Tempo busca linear: {fim - inicio}')

    inicio = time.perf_counter()
    print(binaria(numeros, -90))
    fim = time.perf_counter()
    print(f'Tempo busca binaria: {fim - inicio}')