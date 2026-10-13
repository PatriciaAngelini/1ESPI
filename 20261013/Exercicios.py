# Exercício 1: Somatório de 1 a N
# Escreva uma função recursiva em Python que recebe como entrada um número inteiro
# positivo N e retorna o somatório de todos os números inteiros no intervalo de 1 a
# N .
# Por exemplo, para
# N = 5:
# 5 + 4 + 3 + 2 + 1 = 15

def soma_n(n):
    if n <= 0:
        return 0
    else:
        return n + soma_n(n-1)

# Escreva uma função recursiva em Python que receba dois números inteiros
# o resultado de
# A^B . Considere que o resultado de
# A e B e calcule
# A^B é igual a
# A * A^(B-1) .
# Por exemplo: o resultado de
# 4^5 pode ser calculado como:
# 4^5 = 4 * 4^4
# 4^4 = 4 * 4^3
# 4^3 = 4 * 4^2
# 4^2 = 4 * 4^1
# 4^1 = 4 * 4^0
# 4^0 = 1
def potencia(n, e):
    if e < 0:
        return 1
    else:
        return n * potencia(n, e-1)

# Exercício 3: Busca em uma lista
# Escreva uma função recursiva para realizar uma busca em uma lista de números. A função
# deve receber como parâmetros a lista e um item para buscar na lista. Deve retornar
# caso o item seja localizado, ou
# False , caso não seja localizado
def busca (lista, n):
    if len(lista) == 0:
        return False
    else:
        if lista[0] == n:
            return True
        else:
            busca(lista[1:], n)

# Exercício 4: Contando ocorrências
# Escreva uma função recursiva que recebe como parâmetros uma lista de números inteiros e
# um número inteiro N. A função deve retornar a quantidade de vezes que
# N aparece na
# lista.
def conta_ocorrencia(lista, n):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] == n:
            return 1 + conta_ocorrencia(lista[1:], n)
        else:
            return conta_ocorrencia(lista[1:], n)

# Exercício 5: Máximo divisor comum (MDC)
# O máximo divisor comum (MDC) de dois números inteiros x e y é o maior inteiro que
# dividex e y ao mesmo tempo, e pode ser calculado de acordo com a definição abaixo.
# Escreva uma função recursiva em Python que calcule o MDC de dois números inteiros
# positivos.
# mdc(x, y) = y,
# mdc(y, x),
# se x >= y e x % y == 0
# se x < y
# mdc(y, x % y), caso contrário
# Por exemplo, o MDC de 12 e 18 é 6, pois 6 é o maior número que divide 12 e 18 ao mesmo
# tempo.
def mdc(x,y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return mdc(y,x)
    else:
        return mdc(y,x%y)


# Exercício complementar 4: Árvore genealógica em JSON
# Considere um arquivo JSON que representa a árvore genealógica de uma família. Cada
# pessoa é representada como um dicionário com a chave
# "nome" para o nome e a chave
# "filhos" (se houver) para uma lista de filhos. Cada filho também é um dicionário.
# Criar uma função recursiva que percorre um arquivo JSON nesse formato e exibe os nomes
# de todas as pessoas da família. Considere diferentes arquivos, com diferentes níveis
# hierárquicos (
# familia1.json a
# familia5.json , fornecidos junto com a aula).

def listar_pessoas(dicionario):
    if "filhos" not in dicionario:
        print(dicionario['nome'])
        return
    else:
        print(dicionario['nome'])
        for filho in dicionario['filhos']:
            listar_pessoas(filho)


import json
if __name__ == '__main__':
    print(soma_n(5))
    print(potencia(4, 5))
    lista = [5,7,9,12,5,7,5]
    if busca(lista, 5) == True:
        print('Achou')
    print(conta_ocorrencia(lista, 5))
    lista2 = ['amor', 'carinho', 'paz', 'amor']
    print(conta_ocorrencia(lista2,'amor' ))
    print(mdc(12,18))
    print(mdc(6,3))

    with open('familia1.json', 'r', encoding='utf-8') as f:
        dicio = json.load(f)
        listar_pessoas(dicio)