#Listas
#Colecao flexivel

minhaLista = ['cafe', 'açucar', 'agua']
print(minhaLista)

#Indexacao
#   0       1       2
#  -3      -2      -1
#['cafe', 'açucar', 'agua']
#sempre : o primeiro elemento é o zero e o ultimo é -1
print(f'Primeiro elemento: {minhaLista[0]}')
print(f'Ultimo elemento (indice negativo): {minhaLista[-1]}')
print(f'Ultimo elemento (indice positivo): {minhaLista[2]}')
print('\n\n')
minhaLista = ['cafe', 'açucar', 'agua', 'chantilly', 'canela']
print(minhaLista)
#Slicing - fatiamento
#   0        1       2           3           4
#   -5      -4       -3         -2          -1
#['cafe', 'açucar', 'agua', 'chantilly', 'canela']

#SINTAXE lista[inicio:fim-1:pulo] - o mesmo racional do RANGE

#da esquerda para direita ==> (+1)
#da direita para esquerda <== (-1)

parteLista = minhaLista[2:4+1]
print(f'parte a lista: {parteLista}')
print(f'equivale a fazer sem o final: {minhaLista[2:]}')
print(f'equivale no lado negativo: {minhaLista[-3:]}')
print(f'invertendo: {minhaLista[3:1-1:-1]}')
print(f'pulando: {minhaLista[0::2]}')
print(f'pulando equivalente: {minhaLista[0:5:2]}')
#Concatenacao
#Juntar duas listas
print('\nJuntando duas listas')
print('+')
complementos = ['raspas de limao']
minhaLista = minhaLista + complementos
print(minhaLista)
print('extend')
maiselementos = ['pimenta']
minhaLista.extend(maiselementos)
print(minhaLista)
#Alteracao
print('\nAlterando um elemento')
minhaLista[5] = 'raspas de laranja'
print(minhaLista)
#Inclusao
print('\nIncluindo')
print('append - insere no final')
minhaLista.append('gengibre')
print(minhaLista)
print('insert - insere em uma posicao 3')
minhaLista.insert(3, 'chocolate em po')
print(minhaLista)
#Exclusao
print('\nExclusao')
print('pop')
minhaLista.pop()
print(minhaLista)
print('pop de um posicao 3')
minhaLista.pop(3)
print(minhaLista)
print('Apagando a Lista')
del minhaLista
#Sort
print('\nSort')
minhaLista = ['cafe', 'açucar', 'agua', 'chantilly', 'canela', 'raspas de laranja', 'pimenta']
print(minhaLista)
minhaLista.sort()
print(minhaLista)

import random

teste = ['agua', 'açucar', 'cafe', 'canela', 'chantilly', 'pimenta', 'raspas de laranja']
print(teste)
print(f'tamanho: {len(teste)}')
aleatorio = []
indices_sorteados = []
while len(aleatorio) != len(teste): #garantir qe no final as 2 listas tenham o mesmo tamanho
    indice_sorteado = random.randint(0,6)
    if indice_sorteado not in indices_sorteados:
        aleatorio.append(teste[indice_sorteado])
    indices_sorteados.append(indice_sorteado)
print(aleatorio)

#Matriz nada mais é que lista dentro de lista
print('Matriz')
matriz = [[0, 1, 2], [3, 4, 5]]
print(matriz)
print('Alterando o valor 2 para 8')
matriz[0][2] = 8
print(matriz)
matriz = [[0, 1, 2], [3, 4, 5]]
print('Imprimindo elemento a elemento')
for linha in matriz:
    for coluna in linha:
        print(coluna)
#0 1 2
#3 4 5
print('Imprimindo no formato matriz')
for linha in matriz:
    for coluna in linha:
        print(coluna, end='\t')
    print()
