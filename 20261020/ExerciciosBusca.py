def linear_numero_comparacoes(lista, n):
    # for elemento in lista:
    #     if elemento == n:
    #         return lista.index(elemento)
    # return -1
    contador = 0
    for i in range(len(lista)):
        contador += 1
        if lista[i] == n:
            return contador
    return contador



def binaria_numero_comparacoes(lista, n):
    inicio = 0
    fim = len(lista)-1
    contador = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        contador += 1
        if lista[meio] == n:
            return contador
        elif n < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return contador

if __name__ == '__main__':
    print('Medindo o tempo preciso')
    import time
    numeros = list(range(50000000))

    inicio = time.perf_counter()
    print(f'Comparacoes busca linear:{linear_numero_comparacoes(numeros, -90)}')
    fim = time.perf_counter()
    print(f'Tempo busca linear: {fim - inicio}')
    inicio = time.perf_counter()
    print(f'Comparacoes busca binaria:{binaria_numero_comparacoes(numeros, -90)}')
    fim = time.perf_counter()
    print(f'Tempo busca binaria: {fim - inicio}')