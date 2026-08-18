#Ex2
#lambda par_ou_impar
par_ou_impar = lambda n: f'{n} é par' if n %2 == 0 else f'{n} é impar'
print(par_ou_impar(4))
print(par_ou_impar(-987))

#Ex3
# Dada a lista precos = [100.0, 250.0, 39.90] , use map com uma função lambda para gerar
# uma nova lista com 10% de desconto aplicado a cada preço.
precos:list[float] = [100.0, 250.0, 39.90]
precos_descontados = list(map((lambda n: round(n*0.9,2)),precos))
print(precos_descontados)

#desafio
precos = [100.0, 250.0, 39.90]
descontos = [0.1, 0.2, 0.05]

#RACIONAL, pegar um caso e fazer um DEF para resolver isso
preco = 100
desconto = 0.1
def calculo_desconto (p, d):
    return p * (1-d)

print(f'Com {desconto} de desconto meu preco R${preco:.2f} será '
      f'R${calculo_desconto(preco, desconto):.2f}')

precos = [100.0, 250.0, 39.90]
descontos = [0.1, 0.2, 0.05]
precos_descontos = list(map(calculo_desconto,precos,descontos))
print(precos)
print(precos_descontos)

precos_descontos = list(map((lambda p, d: round(p * (1-d), 2)),
                            precos,descontos))
print(precos_descontos)

#Ex 4
# Crie uma função (com def , não lambda)
# chamada para_maiuscula que receba um texto e
# devolva o mesmo texto em letras maiúsculas.
# Depois, use map para aplicar essa função a
# toda a lista nomes = ["ana", "bruno", "carla"] .
def maiusculo(palavra):
    return palavra.upper()
nomes = ["ana", "bruno", "carla"]
nomes_maiusculo = list(map(maiusculo, nomes))
print(nomes_maiusculo)
nomes_maiusculo2 = list(map((lambda palavra:palavra.upper()), nomes))
print(nomes_maiusculo2)

# Exercício 5
# Dada a lista numeros = [2, 3, 4, 5] , use reduce (com uma função def chamada
# multiplicar ) para calcular o produto de todos os números da lista.

from functools import reduce
def mutiplica (m, n):
    return m*n
numeros = [2, 3, 4, 5]
total = reduce(mutiplica, numeros)
print(total)

#6.
# Dada a lista numeros = [15, 42, 8, 99, 23] ,
# use reduce com uma função lambda para
# encontrar o maior valor da lista, sem usar a função pronta max() .
from functools import reduce

lmaior = lambda x, y: x if x > y else y

numeros = [15, 42, 8, 99, 23]
maior_numero_lista = reduce(lmaior, numeros)
print(maior_numero_lista)
maior_numero_lista2 = reduce((lambda x, y: x if x > y else y),
                            numeros)
print(maior_numero_lista2)