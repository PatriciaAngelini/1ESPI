"""
COLECOES

São variáveis de memoria que tem multiplos valores
Cada valor é chamado de item (ou elemento) que podem ser do mesmo tipo de dado
ou de tipos diferentes: homogeneas ou heterogeneas respectivamente

TODA coleção é um elemento ITERAVEL
significa que pode ir de um em um
que é percorrivel

Há vários tipos de coleções: LISTAS, CONJUNTOS(SET),
TUPLAS, DICIONARIOS(formulario, chave/valor)
"""
"""
LISTA
Caracteristicas
poderosa, flexivel, performatica, conjunto de comandos para manipulacao completos
MUTAVEL: depois de criada, a lista permite acrescentar, retirar, modificar elementos
EXPANSIVEL:pode aumentar seu conjunto de dados a partir de outra lista
ACEITA TIPOS DIFERENTES DE DADOS
INDEXADA: cada elemento tem uma POSICAO dentro da LISTA
PERMITE DUPLICADOS
ORDENAVEIS --> a ordenacao natural so acontece se todos elementos forem do mesmo tipo
SIMBOLO: []
"""

titulo = 'Listas'
print(f'{titulo:^30}')
minhaLista=['café', 'água', 'açucar']
print(minhaLista)

#E se eu quisesse imprimir somente o café?
#Entender como acessar cada elemento pelo índice
#TODA COLECAO INDEXADA COMEÇA NO ZERO
minhaLista=['café', 'água', 'açucar','canela','café']
print(minhaLista)

#0          1        2       3       4
#-5        -4       -3      -2       -1
#'café', 'água', 'açucar','canela','café'
print(f'primeiro elemento:{minhaLista[0]}')
print(f'primeiro elemento:{minhaLista[-5]}')
print(f'segundo elemento:{minhaLista[1]}')
print(f'tamanho da lista:{len(minhaLista)}')
print(f'ultimo elemento:{minhaLista[4]}')
print(f'ultimo elemento:{minhaLista[len(minhaLista)-1]}')
print(f'ultimo elemento:{minhaLista[-1]}')



#tentando acessar um indice que não existe
#print(f'ultimo elemento:{minhaLista[5]}')

#como acrescentar itens numa lista?
#O metodo append faz isso e ACRESCENTA NO FINAL
print('\n')
print(minhaLista)
minhaLista.append('chantilly')
minhaLista.append('especiarias')
print(minhaLista)

#e para remover itens da lista
#usamos o metodo pop
#ele sem paramentro remove DO FIM DA LISTA
minhaLista.pop()
print(minhaLista)
minhaLista.pop()
print(minhaLista)
#MAS EU POSSO REMOVER UM ITEM ESPECIFICO COM O POP
#BASTA PASSAR O INDICE
#removendo o açucar
minhaLista.pop(2)
print(minhaLista)

#TOD O ELEMENTO ITERAVEL podemos percorrer através do FOR
print('Elementos um a um')
for item in minhaLista:
    print(item)
print('\n')
#percorrendo a lista pelos  INDICES da lista
for i in range(len(minhaLista)):
    print(minhaLista[i])

