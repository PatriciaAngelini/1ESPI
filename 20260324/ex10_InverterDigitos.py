print('Inverter digitos')
numero = int(input('Entre com o numero inteiro de 3 digitos: '))
c = numero // 100
resto = numero % 100
d = resto // 10
u = resto % 10

print(f'Numero Original:{numero}, Numero Invertido:{u}{d}{c}')