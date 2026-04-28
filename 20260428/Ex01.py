"""
Solicite 10 numeros inteiros e separe em listas e pares e impare
"""
titulo='Pares e Impares'
print(f'{titulo:^30}')
#Com while
i = 1
# par = []
# impar = []
par, impar = [], []
while i <= 10:
    n = int(input('Entre com o numero inteiro: '))
    #o numero par quer dizer que é divisivel por 2
    #divisivel: o resto da divisao é zero
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    i += 1
print(f'Pares:{par}')
print(f'Impares:{impar}')