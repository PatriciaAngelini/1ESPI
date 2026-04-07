"""
Faça um algoritmo que solicita ao usuário dois números inteiros. O primeiro é o valor das horas e o
segundo dos minutos. Verifique se a hora é válida ou inválida e exiba uma mensagem correspondente
(São válidas as horas entre 00:00 e 23:59)
"""

horas = int(input('Informe as horas: '))
minutos = int(input("Informe os minutos: "))

if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59:
    print(f'{horas:02}:{minutos:02} é uma hora VÁLIDA')
else:
    print(f'{horas:02}:{minutos:02} é uma hora INVÁLIDA')
