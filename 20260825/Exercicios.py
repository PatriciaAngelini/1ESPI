#7. Use list comprehension para
# criar uma lista com os quadrados dos numeros 1 a 10

numeros = [1,2,3,4,5,6,7,8,9,10]
quadrados = [n**2 for n in numeros]
print(quadrados)

quadrados = [n ** 2 for n in range (1,11)]
print(quadrados)

#7.a
#Peca o numero inicial ao usuario, peca o numero final
#Usando list comprehension, calcule os quadrados dos numeros entre
#o numero inicial e o numero final
inicial = int(input('Entre com o numero inicial: '))
final = int(input('Entre com o numero final: '))

quadrados = [n ** 2 for n in range (inicial,final+1)]
print(quadrados)

#8.Dada a lista, use list comprehensiona para criar uma nova lista com pares
numeros = [3,8,15,22,7,40,11]

pares = [n for n in numeros if n%2==0]

#9.Dada lista, crie um nova lista informando par ou impar
numeros = [3,8,15,22,7,40,11]
pares_impar = ['PAR' if n%2==0 else 'IMPAR' for n in numeros]
print(pares_impar)
numeros = [3,8,15,22,7,40,11]
pares_impar = [[n, 'PAR'] if n%2==0 else [n, 'IMPAR'] for n in numeros]

print(pares_impar)
#10. Dada a lista de produtos, use list comprehension para criar uma
#list com os nomes e produtos com estoquem menor que 10

produtos = [
    ['Caderno', 12.50, 5],
    ['Caneta', 2.30, 100],
    ['Mochila', 89.90, 3],
    ['Estojo', 15.00, 8]
]
NOME = 0
PRECO = 1
ESTOQUE = 2
produtos_abaixo_estoque =\
    [prod[NOME] for prod in produtos if prod[ESTOQUE] < 10]
print(produtos_abaixo_estoque)