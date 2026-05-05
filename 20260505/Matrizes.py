#Matrizes sao representadas como lista de listas
#   1   2   3
#   4   5   6
#   7   8   9
print('Matrizes')
matriz = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print(matriz)
#Cada linha é um elemento na matriz principal
#Para acessar um elemento eu devo usar um par ordernado
#Par acessar o 5, o por exemplo, sabemos que ele esta linha 1 e na coluna 1
#linha      0           1          2
#coluna   0  1  2    0  1  2    0, 1, 2
#       [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Elemento do meio da matriz: {matriz[1][1]}')
print(f'Numero 3: {matriz[0][2]}')
print(f'Numero 9: {matriz[2][2]}')
print(f'Numero 6: {matriz[1][2]}')
#como mudar o valor do numero 6 para 101
matriz[1][2]=101
print(matriz)