titulo = "Comprar ou não"
print(f'{titulo:^30}')

dinheiro = float(input('Entre qt dinheiro vc tem em mãos: '))
custo = float(input('Entre custo da mercadoria: '))

if dinheiro >= custo:
    print('Você pode comprar')
else:
    print('Economize mais')