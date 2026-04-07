"""
Faça um algoritmo que solicita ao usuário três valores correspondentes aos lados de um triângulo.
Informe se o triângulo é equilátero (possui 3 lados iguais), isósceles (possui dois lados iguais) ou
escaleno (não possui lados iguais).
"""

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if a == b == c:               # 3 lados iguais
    print('Equilátero')
elif a == b or a == c or b == c:    # 2 lados iguais
    print('Isósceles')
else:                               # todos diferentes
    print('Escaleno')
