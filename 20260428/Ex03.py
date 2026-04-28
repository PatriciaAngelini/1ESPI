titulo = 'Impares de 1 a 100'
print(f'{titulo:^30}')
for i in range(1,100+1,2):
    print(i, end = ' ')
print('\n2a maneira')
for i in range(1,100+1):
    if i % 2 != 0:
        print(i, end = ' ')