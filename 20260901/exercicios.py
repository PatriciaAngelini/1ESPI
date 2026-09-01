# numeros = input('Entre com 3 numeros inteiros: ')
# print(numeros)
# n = numeros.split(',')
# print(n)
# Exercício 1 Crie a tupla
# resto
# , imprimindo os dois valores.
# notas = (7.5, 8.0, 6.5, 9.0)
#  e imprima a primeira nota e a última nota, usando
# índice positivo para a primeira e índice negativo para a última.
print('Ex1')
notas = (7.5, 8.0, 6.5, 9.0)
print(notas)
print(f'Primeira nota: {notas[0]}')
print(f'Ultima nota: {notas[-1]}')



# Exercício 2 Dada a tupla calcule a soma dos elementos sem usar sum
print('\nEx2')
numeros = (12, 45, 7, 23, 9, 31)
total = 0
for numero in numeros:
    total += numero
print(total)


# Exercício 3 Escreva uma função receba uma tupla e conte os pares
print('\nEx3')
def conta_pares(numeros: tuple):
    total = 0
    for numero in numeros:
        if numero % 2 == 0:
            total += 1
    return total
print(f'Total de pares: {conta_pares((12, 45, 7, 23, 9, 31))}')

def tupla_pares(numeros: tuple):
    return tuple([n for n in numeros if n % 2 == 0])

print(f'Pares: {tupla_pares((12, 45, 7, 23, 9, 31))}')

# Exercício 4 Crie duas tuplas de nomes de produtos,
# produtos_loja1 = ("Caneta", "Caderno", "Mochila")
# e
# produtos_loja2 = ("Estojo", "Régua")
# . Concatene as duas tuplas em uma única tupla
# todos_produtos
#  e
# imprima o resultado.
print('\nEx4')
produtos_loja1 = ("Caneta", "Caderno", "Mochila")
produtos_loja2 = ("Estojo", "Régua")
#falsa concatenação
print('Falsa concatenacao')
todos_produtos = (produtos_loja1, produtos_loja2)
print(todos_produtos)
#real concatenacao é com a soma
print('Falsa concatenacao com soma')
todos_produtos = (produtos_loja1 + produtos_loja2)
print(todos_produtos)


# Exercício 5 Dada a tupla
# tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)
# , imprima, usando fatiamento: (a) os
# 4 primeiros elementos; (b) os 3 últimos elementos; (c) a tupla invertida.
print('\nEx5')
tupla = (3, 15, 7, 42, 8, 19, 4, 26, 11)
print('Quatro elementos', tupla[0:4])
print('Tres ultimos elementos', tupla[-3:])
print('Invertido',tupla[::-1])
# Exercício 6 Escreva uma função
# calcular_maior_menor
#  que receba uma tupla de números e retorne
# uma tupla
# (maior, menor) #  com o maior e o menor valor encontrados.
print('\nEx6')
def menor_maior(numeros: tuple) -> tuple:
    maior = max(numeros)
    menor = min(numeros)
    return (menor, maior)
print(f'maior menor: {menor_maior((3, 15, 7, 42, 8, 19, 4, 26, 11))}')



# Exercício 7 Comece com a lista
# lista_nomes = ["Ana", "Bruno", "Carla"]
# . Converta essa lista em uma
# tupla
# tupla_nomes
# . Em seguida, como a tupla não pode ser alterada, converta-a de volta para lista,
# adicione o nome
# "Diego"
#  e converta essa lista final novamente em tupla. Imprima o resultado de cada
# etapa.
print('\nEx7')
lista_nomes = ["Ana", "Bruno", "Carla"]
lista_nomes = tuple(lista_nomes)
print(lista_nomes)
lista_nomes = list(lista_nomes)
print(lista_nomes)
lista_nomes.append('Diego')
tupla_nomes = tuple(lista_nomes)
print(tupla_nomes)
del lista_nomes

# Exercício 8 Represente uma tabela de notas de 3 alunos, em 3 disciplinas cada, como uma tupla de
# tuplas (uma "matriz imutável"):
# notas = ((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0))
# . Escreva
# uma função
# media_aluno
#  que receba essa tupla de tuplas e o índice de um aluno, e retorne a média das
# notas desse aluno.
print('\nEx8')
notas = ((7.0, 8.5, 6.0), (9.0, 7.5, 8.0), (5.5, 6.5, 7.0))
indice_aluno = int(input('Insira o indice do aluno: '))
media = round(sum(notas[indice_aluno])/len(notas[indice_aluno]), 1)
print(media)