#Tupla
#é também uma coleção
#ela é IMUTAVEL: GABRIELA - nasce e morre do mesmo jeito
#ela é indexada (posicional), ela é heterogenea

print('TUPLA')
minhaTupla = ('sol', 'agua', 'natureza')
#   0      1         2
#   -3     -2        -1
#('sol', 'agua', 'natureza')
print(minhaTupla)

print('\nTipos de dados diferentes')
outraTupla = tuple(('a', 45, True))
print(type(outraTupla))
print(outraTupla)

print('\nAcessando pela posicao')
print(f'1a posicao:{minhaTupla[0]}')
print(f'2a posicao:{minhaTupla[1]}')
print(f'ultima posicao:{minhaTupla[-1]}')

print('\nPegadinha 1 - tupla vazia')
#nao faz sentido criar uma tupla vazia, pois nao podemos acrescentar elementos
tuplavazia = ()
print(tuplavazia)

print('\nPegadinha  - tupla de um elemento precisa de virgula')
tuplaumfalsiane = ('sol')
print(tuplaumfalsiane)
print(type(tuplaumfalsiane))

tuplaum = ('sol',)
print(tuplaum)
print(type(tuplaum))

print('\nAchando a posica de um elemento')

#               0      1         2        3
#               -4      -3     -2        -1
minhaTupla = ('sol', 'agua', 'natureza', 'sol')
print(minhaTupla)
print(f'A agua esta na posicao: {minhaTupla.index('agua')}')
print(f'O 1o sol esta na posicao: {minhaTupla.index('sol')}')
print(f'O proxim sol esta na posicao: {minhaTupla.index('sol', 1)}')
#               0       1        2         3     4       5       6
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(f'O 1o sol esta na posicao: {minhaTupla.index('sol')}')
print(f'O 2o sol esta na posicao: {minhaTupla.index('sol',minhaTupla.index('sol') + 1)}')
#a partir da 2a ocorrencia nao é mais "legivel"
print(f'O 3o sol esta na posicao: {minhaTupla.index('sol', minhaTupla.index('sol',minhaTupla.index('sol') + 1) + 1)}')

print('\nPercorrendo a colecao toda')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(minhaTupla)
for item in minhaTupla:
    print(item)



#               0       1        2         3     4       5       6
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print('\nAchando a posicoes dos sois')
#o enumerate traz o par (indice, item)
#e ai usamos a atribuicao multipla do python para colocar nas respectivas variaveins
#for n, elemento in enumerate(minhaTupla):
for indice, item in enumerate(minhaTupla):
    if item == 'sol':
        print(f'posicao {indice}: {minhaTupla[indice]}')

print('\nMatriz de tuplas')
matrizTupla =(('cafe', 'banho'),('almoco', 'academia'), ('aula', 'series'))
print(matrizTupla)
print(matrizTupla[2][1])

#Unpacking - atribuicao multipla
print('\nUnpacking')
pessoa = ('Patricia', 'Casada', 54)
nome, estado_civil, idade = pessoa
print(nome)
print(estado_civil)
print(idade)

print('\nConversao para gambiarrar')
minhaTupla = ('sol', 'agua', 'natureza', 'sol', 'sol', 'lago', 'sol')
print(minhaTupla)
#Acrescentar um elemento ???? nao tem append
#como fazer
temp = list(minhaTupla)
temp.append('chuva')
print(type(temp))
minhaTupla = tuple(temp)
print(minhaTupla)
del temp