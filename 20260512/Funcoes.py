#Funcoes
#Para organizar o codigo
#Para reaproveitamento
#Primo pobre do microservico

#Sintaxe
#def nome_funcao(parametros separados por virgula):
#   instrucoes
#   return expressao

#1o passo é a definicao da funcao
#2o passo é o uso

print('Funcoes')
print('Funcao simples')
#1o passo
def OlaMundo ():
    print('Ola Mundo')

#2o passo
OlaMundo()

#Funcao com parametros
#A gente define o parametro apenas dizendo o seu nome
#Nao precisamos definir o tipo do parametro
print('\nFuncao com parametro e uso posicional')
def Soma (p1, p2):
    total = p1 + p2
    print (total)

print('O total é:', end=' ')
Soma(5,6)

print('\nFuncao com parametro e uso nomeado')
def Subtracao(p1, p2):
    total = p1 - p2
    print(total)
print('Posicional')
print('O total é:', end=' ')
Subtracao(5,6)

print('Nomeado')
print('O total é:', end=' ')
Subtracao(p2=8, p1=5)

print('\nEscopo')
#Escopo
#No python e em qq linguagem há uma discussao sobre escopo
#O escopo é a VISIBILIDADE da variavel
#Existem variaveis de ESCOPO GLOBAL e variaveis e ESCOPO LOCAL
#No escopo GLOBAL as variveis sao definidas no programa principal
clima = 'inverno' #o clima é de escopo global
def MostraClima():
#percebemos que mesmo DENTRO DA FUNCAO conseguimos acessar o
#valor da variavel clima
    print(f'O clima de hoje é de {clima}')

MostraClima()

#a unica regra é que variavel global NÃO PODE estar definida
#DEPOIS DA FUNCAO
#
# def MostraClima2():
# #percebemos que mesmo DENTRO DA FUNCAO conseguimos acessar o
# #valor da variavel clima
#     print(f'O clima de hoje é de {clima2}')
# #Se usarmos a funcao antes de definir a variavel GLOBAL
# #Ela apresenta um erro
# MostraClima2()
# clima2 = 'verao'
# #Em outras linguagens mesmo definindo a variavel antes da chamada
# #da funcao, ela nao funcionaria
# clima2 = 'verao'
# MostraClima2()

#E se nós tivessemos um variavel que fosse definida DENTRO DA FUNCAO?
#Ou seja ESCOPO LOCAL
#Será que conseguiriamos ver o valor dela no programa principal

def MostraTemperatura():
    temperatura = 13
    print(f'A temperatura hoje é de {temperatura} graus')

MostraTemperatura()

def DefineTemperatura():
    #A variavel aqui tem escopo local
    #Ou seja, não conseguimos acessar seu valor
    #no programa principal
    temp = 14
#Isso nao funciona
# DefineTemperatura()
# print(f'A temperatura é de {temp}')

print('\nRetorno da Funcao')

def Soma2 (p1, p2):
    total = p1 + p2
    return total

#o def permite que usemos direto em outras funcoes
n1 = 8
n2 = 9
print(f'A soma de {n1} e {n2} é {Soma2(n1, n2)}')

def Saudacao (nome):
    return 'Bom dia ' + nome + '!'

print(Saudacao('Leticia'))