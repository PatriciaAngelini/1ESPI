titulo = 'Estrutura Repeticao While'
print(f'{titulo:^30}')
"""
se a gente quisesse calcular a tabuada do 3 teriamos 
que fazer a mesma operacao 10 X
"""
# numero = 3
# print(f'{numero} X 1 = {numero*1}')
# print(f'{numero} X 2 = {numero*2}')
# print(f'{numero} X 3 = {numero*3}')
# print(f'{numero} X 4 = {numero*4}')

#while -> enquanto
#a minha repeticao esta estruturada enquanto a
#comparacao (condicao) for verdadeira
#o while é muito parecido com o if
#mas funcionando somente do lado verdadeiro

# #para o calculo da tabuada, preciso repetir
# #a mesma operacao 10 X
# numero = int(input('Escolha um numero para tabuada: '))
# i = 1
# while i <= 10:
#     tabuada = i * numero
#     print(f'{numero} X {i} = {numero*i}')
#     i = i + 1

#colocando o incremento como primeira instrução
#ele começa no 2 e vai até o 11
# numero = int(input('Escolha um numero para tabuada: '))
# i = 1
# while i <= 10:
#     i = i + 1
#     tabuada = i * numero
#     print(f'{numero} X {i} = {numero*i}')

#pulando de 2 em 2
# numero = int(input('Escolha um numero para tabuada: '))
# i = 1
# while i <= 10:
#     tabuada = i * numero
#     print(f'{numero} X {i} = {numero*i}')
#     i = i + 2

# #perguntando ao usuario se ele quer continuar
# numero = int(input('Escolha um numero para tabuada: '))
# i = 1
# resp = 's'
# while resp == 's':
#     tabuada = i * numero
#     print(f'{numero} X {i} = {numero*i}')
#     i += 1 # equivale i = i + 1
#     resp = input('Quer calcular + 1?: ').lower()[0]

# #Calcular a tabuada inteira (de 1 a 10)
# #E se o usuario quiser calcular a do proximo numero
# #Faca isso enquanto o usuario responder sim
# numero = int(input('Escolha um numero para tabuada: '))
# i = 1
# resp = 's'
# while resp == 's':
#     while i <= 10:
#         tabuada = i * numero
#         print(f'{numero} X {i} = {numero*i}')
#         i += 1 # equivale i = i + 1
#     i = 1
#     resp = input('Quer calcular a prox tabuada?: ').lower()[0]
#     numero += 1

#Matheus Medeiros
titulo = 'Estrutura Repeticao While'
print(f'{titulo:^30}')

numero = int(input('Escolha um numero para tabuada: '))
i = 1
resposta = "s"
while i <= 10 and resposta == "s":
        tabuada = i * numero
        print(f'{numero} X {i} = {tabuada}')
        i = i + 1
        if i == 11:
            resposta = input("Deseja continuar? ").lower()[0]
            i = 1
            numero = numero + 1