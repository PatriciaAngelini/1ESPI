"""
Faça um algoritmo que solicita ao usuário um valor inteiro e exibe uma mensagem
informando se o número é par ou ímpar.
"""

numero = int(input('Digite um numero inteiro: '))
if numero % 2 == 0:
    print('Par')
else:
    print('Ímpar')
