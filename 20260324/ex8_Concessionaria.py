print('Concessionaria')
vendedor = input('Entre com o nome do vendedor: ')
qt = int(input('Entre com a quantidade de carros do ' + vendedor + ': '))
vl = float(input('Entre com o valor total de vendas do ' + vendedor + ': '))
tx = 0.02
salario_base = 2500
vl_por_carro = 200

salario = salario_base + (qt*vl_por_carro) + (vl*tx)

print(f'O salario do {vendedor} será de R${round(salario, 2)}')
#print(f'O salario do {vendedor} será de R${round(salario, 2)}')