"""30 Numeros aleatorios de 1 a 50. a partir dessa lista, deixe so
os numeros primos
"""
import random
titulo = 'Somente os primos'
print(f'{titulo:30}')
numeros = []
for i in range(30):
    numeros.append(random.randint(1, 50))
print(numeros)
primos = []
for numero in numeros:
    primo = True
    for divisor in range (2, numero):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        #print('é primo')
        primos.append(numero)
print(primos)


#teste para um numero
# n = 7
# primo = True
# for divisor in range (2, n):
#     if n % divisor == 0:
#         primo = False
#         break
# if primo:
#     print('é primo')
# else:
#     print('nao é primo')