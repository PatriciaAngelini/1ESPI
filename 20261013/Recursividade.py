#Recursividade é a estrategia de quebrar um problema em partes menores até
#um problema conhecido
#Ex = 5! => 5x4!, 4! => 4x3!, .... 1!=1x0!, 0!=1
#0! é chamado de condicao base, que a solucao de um problema conhecido

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))

#problema somar os elementos de uma lista
#fazer uma funcao recursiva
lista = [3,5,678,3,78,90]
def soma_lista_sem_recursao(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
print(soma_lista_sem_recursao(lista))

def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
print(soma_lista(lista))