horas = int(input('Informe as horas: '))
minutos = int(input("Informe os minutos: "))

if 0 <= horas <= 23 and 0 <= minutos <= 59:
    print(f'{horas:02}:{minutos:02} é uma hora VÁLIDA')
else:
    print(f'{horas:02}:{minutos:02} é uma hora INVÁLIDA')
