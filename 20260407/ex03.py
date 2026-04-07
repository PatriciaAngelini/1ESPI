"""
Faça um algoritmo que solicita ao usuário um número inteiro e exiba este número na tela. Se o
número for negativo, antes de ser exibido, ele deve ser transformado no equivalente positivo.
"""

numero = int(input('Digite um número inteiro: '))
if numero < 0:
    numero = numero * -1
print(numero)
