#Dicionarios sao colecoes do tipo formulario
#chave:valor
#Exemplo
#Nome : Patricia
#Idade : 54
#Sexo : Fem
# NAO SAO POSICIONAIS - nao tem indice
# permitem tipo de dados diferente
# permitem valores repetidos, porem CHAVES SAO UNICAS
# permitem inclusao, alteracao, exclusao SAO MUTAVEIS
# simbolo {}
from logging import addLevelName

print('Dicionarios')
aluno = {'nome': 'Patricia', 'idade': 56, 'sexo': 'feminino'}
print(aluno)
print(type(aluno))

print('Acessando valor a valor')
print(aluno['nome'])
print(aluno['idade'])
print(aluno['sexo'])

print('\nDicionario vazio')
vazio = {}
print(vazio)

print('\nAcrescentando valores em um dicionario')
vazio['categoria'] = 'Brinquedos'
print(vazio)
print('\n')
print(aluno)
aluno['profissao'] = 'estagiario'
print(aluno)

print('\nAlterando valores')
aluno['nome'] = 'Andrea'
print(aluno)
print(aluno.get('nome'))
aluno.update({'idade': 18})
print(aluno)

print('\nRemovendo valores')
aluno.pop('idade') #elimina segundo uma chave, pop funciona para dicionario
print(aluno)
del aluno['sexo'] #elimina segundo uma chave, del é uma exclusao generica
print(aluno)
aluno.popitem() #elimina o ultimo
print(aluno)


print('\nLimpa o dicionario')
aluno.clear()
print(aluno)


###ATENCAO###
#Consigo sempre alterar valores
#Mas nunca as chaves
aluno = {'nome': 'Andrea', 'idade': 18, 'sexo': 'feminino', 'profissao': 'estagiario'}
print(aluno)
aluno['profissao'] = 'analista junior'
print(aluno)
#aqui ele nao troca, ele acaba acresentando um valor no dicionario
aluno['profissao carteira'] = 'analista junior'
print(aluno)
#como trocar a chave, precisa eliminar e recriar
del aluno['profissao carteira']
aluno.pop('profissao')
aluno['profissao carteira'] = 'analista junior'
print(aluno)

print('\nPercorrendo ou varrendo o dicionario')
aluno = {'nome': 'Andrea', 'idade': 18, 'sexo': 'feminino', 'profissao carteira': 'analista junior'}
for caracteristica in aluno: #qdo so coloco o nome do dicionario estou pegando as chaves
    print(caracteristica)
print('\nSomente as chaves')
for chave in aluno.keys():
    print(chave)
print('\nSomente os valores')
for valor in aluno.values():
    print(valor)
print('\nSomente os valores pela chaves')
for chave in aluno:
    print(aluno[chave])
print('\nOs itens completos')
for item in aluno.items():
    print(item)
print('\nOs itens ja separados com atribuicao multiplos')
for chave, valor in aluno.items():
    print(f'{chave}={valor}')

#atribuicao multipla
x, y, z = 0, 1, 2
print(f'{x}')
print(f'{y}')
print(f'{z}')


#na maior parte das colecoes a copia se da pela igualdade
#vamos examinar a lista
print('\n\n')
original = ['cafe', 'pao', 'leite']
copiafalsa = original
copia = original.copy()
print('original  ', original)
print('copiafalsa',copiafalsa)
print('copia     ', copia)
copiafalsa.append('cachorro')
copia.append('gato')
print('original  ',original)
print('copiafalsa',copiafalsa)
print('copia     ', copia)

print('\nCopiando o dicionario')
aluno = {'nome': 'Andrea', 'idade': 18, 'sexo': 'feminino', 'profissao carteira': 'analista junior'}
aluno_copia = aluno.copy()
aluno_copia['nome'] = ('Andrea Macedo')
print(aluno)
print(aluno_copia)
