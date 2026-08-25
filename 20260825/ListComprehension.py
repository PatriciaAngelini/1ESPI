print('Revisao Map')
def dobro (n:int) -> int:
    return n * 2

numeros = [7, 87, 90, -23, 4, 0]
print(numeros)
numeros_dobrados = list(map(dobro, numeros))
print(numeros_dobrados)


def mult (n:int, m:int) -> int:
    return n * m

numeros = [7, 87, 90, -23, 4, 0]
print(numeros)
multiplicadores = [2, 3, 4, 5, 6, 7]
multiplicados = list(map(mult, numeros, multiplicadores))
print(multiplicados)

multiplicados2 = list(map((lambda m, n: n * m), numeros, multiplicadores))
print(multiplicados)


print('\nList Comprehension')
#feito para simplificar o map
#retorna uma lista
print('\n sem o list comprehension')
numeros = [7, 87, 90, -23, 4, 0]
dobrados = []
for n in numeros:
    dobrados.append(n * 2)

print(dobrados)
print('\n com o list comprehension')
dobrados2 = [n * 2 for n in numeros]
print(dobrados2)


print('\n com o list comprehension e condicional')
numeros = [7, -87, 90, -23, 4, 0]
dobradospositivos = [n * 2 for n in numeros if n > 0]
print(dobradospositivos)

print('\n com o list comprehension e condicional com else')
numeros = [7, -87, 90, -23, 4, 0]
dobradospositivos100negativos = \
    [n * 2 if n > 0 else n+100 for n in numeros ]
print(dobradospositivos100negativos)