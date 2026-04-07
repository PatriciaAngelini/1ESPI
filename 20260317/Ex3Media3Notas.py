print('Média de três notas')
n1 = float(input('Entre a primeira nota: '))
n2 = float(input('Entre a segunda nota: '))
n3 = float(input('Entre a terceira nota: '))
media = (n1+n2+n3)/3
#o round é uma função que fazo o arredondamento
print(media)
print(round(media,1))
print('A média das 3 notas:', n1, n2, n3, 'é', round(media, 1))