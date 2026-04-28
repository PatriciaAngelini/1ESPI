"""
Há um outra estrutura de repeticao que serve para
quando sabemos de antemao quantas repeticoes vamos ter
FOR
--> percorre ELEMENTOS ITERAVEIS
"""
titulo = 'Estrutura Repeticao FOR'
print(f'{titulo:^30}')

titulo = 'TABUADA'
print(f'{titulo:^30}')
#enquanto o while nós temos que controlar o contador
#o for faz isso de maneira automatica
#1a versao
n=int(input('Entre com um numero inteiro para a tabuada: '))
for numero in (1,2,3,4,5,6,7,8,9,10): #o numero aqui representa um contador
    tabuada = n * numero
    print(f'{n} X {numero} = {tabuada}')
print('\ntabuada com o range')
for i in range(1,11):
    tabuada = n * i
    print(f'{n} X {i} = {tabuada}')
for i in range(10):
    tabuada = n * (i + 1)
    print(f'{n} X {i + 1} = {tabuada}')

"""
existe uma maneira de abreviar essa lista de numeros
é o comando RANGE
range nada mais é que um gerador de numeros de um intervalo
SINTAXE
range(inicio, fim, incremento)
no uso precisamos acrescentar no parametro de fim pois ele come um do final
range(inicio, fim + 1, incremento)

range(quantidade de numeros)
lembrar que desse jeito ele começa no ZERO
"""


# #1a maneira de uso é passar quantidade de numeros necessarios
# print('Gerando 5 numeros')
# for i in range(5):
#     print(i)
# print('\n')
# for i in range(5):
#     print(i+1)
#
# #será q o range pode gerar os numeros a partir de um numero escolhido?
# #por exemplo a partir do 1
# #2a maneira - passando o inicio e final
# print('Gerando 5 numeros a partir de um inicio')
# #desse jeito ele comeu o ultimo numero
# for i in range(1,5):
#     print(i)
# #corrigindo
# print('\n')
# for i in range(1,6):
#     print(i)
# print('\n')
# for i in range(1,5+1):
#     print(i)
#
# #Existe mais um parametro no range
# #o ultimo parametro chamamos de incremento ou pulo
# print('Gerando numeros a partir de um inicio e com pulo de 2 (até a o numero 5)')
# #desse jeito ele comeu o ultimo numero
# for i in range(1,5+1,2):
#     print(i)
