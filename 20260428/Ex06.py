titulo = 'Maior e Menro'
print(f'{titulo:^30}')
for i in range(5):
    n = int(input('Entre com um numero: '))
    if i == 0:
        maior = menor = n
        # maior = n
        # menor = n
        continue # facultativo
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior numero é: {maior} e o menor é: {menor}')