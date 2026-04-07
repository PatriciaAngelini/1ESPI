"""
Faça um algoritmo que solicite dois números
ao usuário e exiba apenas o MAIOR deles.
Caso eles sejam iguais exiba a mensagem
“Números Iguais”.
"""

a = float(input('Informe o primeiro número: '))
b = float(input('Informe o segundo número: '))

if a > b:
    print(f'Maior: {a}')
elif b > a:
    print(f'Maior: {b}')
else:
    print('Números Iguais')

