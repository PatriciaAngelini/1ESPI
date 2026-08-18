#Lambda
#Funcao anonima (pequena - de uma linha só - funçao inline)
#A criacao da funcao estar proxima do uso
#Versateis
#Cuidado que temos que ter, é NAO TENTAR RESOLVER TUDO COM LAMBDA
#Se vc fizer isso o seu programa fica ilegivel

#Numa funcao tradicional fariamos
def dobro (n:int) -> int:
    """
    Calcula o dobro de um numero inteiro

    :param n: numero inteiro
    :return: dobro de um numero inteiro
    """
    return n * 2

#uso
print(dobro(4))

#transformar em lambda
#sintaxe lambda <argumentos/parametros> : <expressao de retorno>
#lambda SEMPRE TEM O RETURN
ldobro = lambda n : n * 2
print(ldobro(79))
#o uso mais comum
print((lambda n: n * 2)(65))


#Lambda CONDICIONAL
#Tem um if embutido

#funcao que decide qual o maior de 2 numeros
def maior(x:int,y: int)->int:
    if x > y:
        return x
    else:
        return y
# uso
print(maior(y=4, x=5))  # <= parametros nomeados

#transformando em lambda
#nao é o uso mais comum
lmaior = lambda x,y: x if x > y else y
print(lmaior(4,5))

#uso mais comum
print((lambda x,y: x if x > y else y)(9,65))

#posso o usar o print dentro do lambda
#pode, mas cuidado
lmenor = lambda x,y: print(x) if x < y else print(y)
xpto = lmenor (123,97)
lmenor (43,2)
# print(lmenor(9,65))

#a melhor solucao
lmenor2 = lambda x,y: \
    f'entre {x} e {y} o numero menor é {x}' \
        if x < y else \
        f'ntre {x} e {y} o numero menor é {y}'
print(lmenor2(8,23))



#Map é uma funcionalidade do python que permite aplicar
#uma funcao em todos os elementos de uma colecao
print('\nMap')
def dobro (n:int) -> int:
    return n * 2
numeros = [7, 87, 90, -23, 4, 0]

print('\nSem o map')
#da maneira roots
dobrados =[]
for n in numeros:
    dobrados.append(dobro(n))
print(numeros)
print(dobrados)

print('\nCom o map')
#com map
#sintaxe map(nome da funcao, iteravel/colecao)
#1o uso criando uma lista de numeros dobrados nova
dobrados2 = list(map(dobro, numeros))
print(dobrados2)
#2o uso direto no print
print(list(map(dobro, numeros)))

print('\nCom o map e o lambda')
#utilizando o ldobro abaixo, como eu faria o map?
ldobro = lambda n : n * 2
dobrado3 = list(map(ldobro, numeros))
print(dobrado3)

#o jeito mais pythoneiro
print(list(map((lambda n: n*3), [23, 4, 876, - 4])))

#REDUCE:
#É uma funcao que aplica um def ou lambda em todos elementos
#de uma colecao (lista) e reduz a um unico elemento
print('\nReduce')
def soma (n:int, m:int) -> int:
    return n+m
print(soma(4, 7))

#import functools as f
from functools import reduce
numeros = [7, 87, 90, -23, 4, 0]
#total = f.reduce(soma, numeros)
total = reduce(soma, numeros)
print(total)












