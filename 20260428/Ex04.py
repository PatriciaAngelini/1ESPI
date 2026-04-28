import random
titulo = '20 numeros aleatorios'
print(f'{titulo:^30}')
for i in range(20):
    print(random.randint(1,50), end = ' ')