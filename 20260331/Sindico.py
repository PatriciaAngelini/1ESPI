titulo = "Sindico"
print(f'{titulo:^30}')

#numero par
bloco = int(input("Entre com o bloco de 1 a 20: "))

if 1<= bloco <= 10:
    print('Sindico Hamilton')
else:
    print('Sindio Jose')

if bloco in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print('Sindico Hamilton')
else:
    print('Sindio Jose')