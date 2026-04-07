"""
Faça um algoritmo que solicita ao usuário
três números e exibe na tela apenas o MENOR
deles, ou uma mensagem informando que os
números são iguais.
"""

a = float(input('Informe o primeiro número: '))
b = float(input('Informe o segundo número: '))
c = float(input('Informe o terceiro número: '))

if a < b and a < c:
    print(f'Menor: {a}')
elif b < a and b < c:
    print(f'Menor: {b}')
elif c < a and c < b:
    print(f'Menor: {c}')
else:
    print('Números Iguais')
