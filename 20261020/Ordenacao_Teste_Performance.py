def bubble_sort(lista: list[int]) -> None:
    """Ordena a lista em ordem crescente com o método da bolha (bubble sort).

    Args:
        lista: lista de números, que será modificada (ordenada no lugar).

    Returns:
        None. A própria lista recebida fica ordenada.
    """
    n = len(lista)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:             # compara itens vizinhos
                aux = lista[j]                      # realiza a troca
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


def selection_sort(lista: list[int]) -> None:
    """Ordena a lista em ordem crescente com o método da seleção (selection sort).

    Args:
        lista: lista de números, que será modificada (ordenada no lugar).

    Returns:
        None. A própria lista recebida fica ordenada.
    """
    n = len(lista)
    for i in range(0, n - 1):
        menor = i
        for j in range(i + 1, n):                   # encontra o índice do menor item
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]                              # realiza a troca
        lista[i] = lista[menor]
        lista[menor] = aux


def insertion_sort(lista: list[int]) -> None:
    """Ordena a lista em ordem crescente com o método da inserção (insertion sort).

    Args:
        lista: lista de números, que será modificada (ordenada no lugar).

    Returns:
        None. A própria lista recebida fica ordenada.
    """
    n = len(lista)
    for i in range(1, n):
        j = i
        while j > 0 and lista[j] < lista[j - 1]:    # compara com o item da esquerda
            aux = lista[j]                          # realiza a troca
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1


def intercala(lista: list[int], inicio: int, meio: int, fim: int) -> list[int]:
    """Intercala duas sublistas ordenadas, vizinhas, de uma mesma lista.

    A primeira sublista vai do índice inicio até meio; a segunda, de
    meio + 1 até fim. O resultado fica ordenado nas posições inicio..fim.

    Args:
        lista: lista que contém as duas sublistas (será modificada).
        inicio: primeiro índice da primeira sublista.
        meio: último índice da primeira sublista.
        fim: último índice da segunda sublista.

    Returns:
        A própria lista recebida, com as posições inicio..fim intercaladas.
    """
    aux = []                                        # lista auxiliar
    esq = inicio
    dir = meio + 1
    while esq <= meio and dir <= fim:               # enquanto nenhuma sublista acabou,
        if lista[esq] <= lista[dir]:                # copia o menor item para aux
            aux.append(lista[esq])
            esq += 1
        else:
            aux.append(lista[dir])
            dir += 1
    while esq <= meio:                              # copia o resto da primeira sublista
        aux.append(lista[esq])
        esq += 1
    while dir <= fim:                               # copia o resto da segunda sublista
        aux.append(lista[dir])
        dir += 1
    lista[inicio:fim + 1] = aux                     # copia aux de volta para a lista
    return lista


def merge_sort(lista: list[int], inicio: int, fim: int) -> None:
    """Ordena uma parte da lista com o método da intercalação (merge sort).

    Args:
        lista: lista de números, que será modificada (ordenada no lugar).
        inicio: primeiro índice da parte a ordenar.
        fim: último índice da parte a ordenar.

    Returns:
        None. A própria lista recebida fica ordenada nas posições inicio..fim.
    """
    meio = (fim + inicio) // 2
    if inicio < fim:
        merge_sort(lista, inicio, meio)             # primeira metade da lista
        merge_sort(lista, meio + 1, fim)            # segunda metade da lista
        intercala(lista, inicio, meio, fim)         # intercala as duas metades


def particionamento(lista: list[int], inicio: int, fim: int) -> int:
    from random import randint
    """Particiona uma parte da lista em torno de um pivô sorteado.

    Ao final, os itens menores ou iguais ao pivô ficam à esquerda dele e
    os maiores ficam à direita.

    Args:
        lista: lista de números (será modificada).
        inicio: primeiro índice da parte a particionar.
        fim: último índice da parte a particionar.

    Returns:
        O índice onde o pivô foi parar.
    """
    indice = randint(inicio, fim)                   # sorteia o índice do pivô
    aux = lista[inicio]                             # leva o pivô para a primeira posição
    lista[inicio] = lista[indice]
    lista[indice] = aux

    pivo = lista[inicio]
    i = inicio                                      # i marca o fim da região dos menores
    for j in range(inicio + 1, fim + 1):
        if lista[j] <= pivo:                        # achou um item menor ou igual ao pivô
            i += 1
            aux = lista[i]                          # leva o item para a região dos menores
            lista[i] = lista[j]
            lista[j] = aux

    aux = lista[inicio]                             # coloca o pivô entre as duas regiões
    lista[inicio] = lista[i]
    lista[i] = aux
    return i


def quick_sort(lista: list[int], inicio: int, fim: int) -> None:
    """Ordena uma parte da lista com o método rápido (quick sort).

    Args:
        lista: lista de números, que será modificada (ordenada no lugar).
        inicio: primeiro índice da parte a ordenar.
        fim: último índice da parte a ordenar.

    Returns:
        None. A própria lista recebida fica ordenada nas posições inicio..fim.
    """
    if inicio < fim:                                # pelo menos 2 itens
        posicao = particionamento(lista, inicio, fim)
        quick_sort(lista, inicio, posicao - 1)      # lado esquerdo do pivô
        quick_sort(lista, posicao + 1, fim)         # lado direito do pivô

if __name__ == "__main__":
    from random import sample
    from datetime import datetime


    # (as funções bubble_sort, selection_sort, insertion_sort, merge_sort e
    # quick_sort da aula vêm antes, no mesmo arquivo)

    def criar_lista():
        """retorna uma lista aleatória com N itens"""
        n = 20000
        lista = sample(range(100000000), n)  # 20 mil números aleatórios diferentes
        return lista


    original = criar_lista()
    lista = original.copy()
    tempo_inicial = datetime.now()
    bubble_sort(lista)
    tempo_final = datetime.now()
    print(f'BubbleSort....: {tempo_final - tempo_inicial}')

    lista = original.copy()
    tempo_inicial = datetime.now()
    selection_sort(lista)
    tempo_final = datetime.now()
    print(f'SelectionSort.: {tempo_final - tempo_inicial}')

    lista = original.copy()
    tempo_inicial = datetime.now()
    insertion_sort(lista)
    tempo_final = datetime.now()
    print(f'InsertionSort.: {tempo_final - tempo_inicial}')

    lista = original.copy()
    tempo_inicial = datetime.now()
    quick_sort(lista, 0, len(lista) - 1)
    tempo_final = datetime.now()
    print(f'QuickSort.....: {tempo_final - tempo_inicial}')

    lista = original.copy()
    tempo_inicial = datetime.now()
    merge_sort(lista, 0, len(lista) - 1)
    tempo_final = datetime.now()
    print(f'MergeSort.....: {tempo_final - tempo_inicial}')

    lista = original.copy()
    tempo_inicial = datetime.now()
    lista.sort()
    tempo_final = datetime.now()
    print(f'Sort Python...: {tempo_final - tempo_inicial}')

    lista = original.copy()
    tempo_inicial = datetime.now()
    lista2 = sorted(lista)
    tempo_final = datetime.now()
    print(f'Sorted Python.: {tempo_final - tempo_inicial}')
