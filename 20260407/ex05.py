"""
Faça um algoritmo que solicita um número inteiro e exibe uma mensagem indicando se ele é positivo,
negativo ou zero.
"""

numero = int(input('Informe um número inteiro: '))
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')

