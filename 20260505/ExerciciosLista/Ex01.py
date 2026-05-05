"""
random.randint(a, b)
Return a random integer N such that a <= N <= b.
Alias for randrange(a, b+1).
"""
"""Preencha uma lista com numeros aleatorios nao repetidos de 1 a 20"""
import random

#teste
#print(random.randint(1, 20))

# numeros = []
# for i in range(10): #gera 10 numeros de 0 a 9
#     #nao podemos fazer direto porque corre o risco de ter repetido
#     #numeros.append(random.randint(1,20))
#     numero = random.randint(1,20)
#     #existe = numeros.index(numero)
#     #nao posso atribuir a uma variavel porque se o numero nao estiver na list
#     #vai estourar um erro
#     while numero in numeros:
#         numero = random.randint(1, 20)
#     numeros.append(numero)
#
# print(numeros)

# teste = [13, 9, 2, 11, 19, 2, 17, 16, 19, 5]
# print(teste.index(10))
# # if 10 in teste:
# #     print('O 10 esta na lista')
# # else:
# #     print('O 10 nao esta na lista')

#versao final
numeros = []
for i in range(10):
    numero = random.randint(1,20)
    while numero in numeros:
        numero = random.randint(1, 20)
    numeros.append(numero)
print(numeros)