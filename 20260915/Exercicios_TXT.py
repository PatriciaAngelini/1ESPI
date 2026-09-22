# — Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de
# texto chamado numeros.txt (um número em cada linha)

# try:
#     arqNum = open('numeros.txt', 'w', encoding='utf-8')
#     for i in range(10):
#         n = int(input(f'Entre com o {i+1} numero inteiro: '))
#         arqNum.write(f'{n}\n')
#     arqNum.close()
# except ValueError:
#     print('Entre com um numero inteiro')
# except Exception as erro:
#     print(f'Ocorreu um erro na linha {erro}')

# Abra o arquivo
# numeros.txt
#  criado no exercício anterior. Leia o conteúdo do
# arquivo e mostre o somatório de todos os números contidos nele
# try:
#     arqNum = open('numeros.txt', 'r', encoding='utf-8')
#     total = 0
#     for linha in arqNum:
#          total += int(linha)
#
#     print(total)
#
#     arqNum.seek(0)
#     total = 0
#     lista_numeros = arqNum.readlines()
#     lista_numeros = [int(x) for x in lista_numeros]
#     print(sum(lista_numeros))
# except FileNotFoundError:
#     print('Arquivo não encontrado')

# Exercício 3 — Faça um programa que crie um arquivo de texto denominado
# arquivo.txt
#  e
# permita que o usuário grave diversos caracteres nesse arquivo até que seja digitado o
# caractere "0" (zero).
# try:
#     arqTXT = open('arquivo.txt', 'w', encoding='utf-8')
#     palavra = input('Digite uma palavra: ')
#     for letra in palavra:
#         if letra != '0':
#             arqTXT.write(letra)
#         else:
#             break
#     arqTXT.close()
# except Exception as e:
#     print(e)

# Exercício 4 — Solicite ao usuário diversos números inteiros (até que seja digitado o número
# zero). Armazene os números pares em um arquivo (
# pares.txt
# ) e os números ímpares em
# outro (
# impares.txt
# )

# try:
#     arqPar = open('pares.txt', 'w', encoding='utf-8')
#     arqImpar = open('impares.txt', 'w', encoding='utf-8')
#     while True:
#         numero = int(input('Digite um numero inteiro ou 0 para sair: '))
#         if numero == 0 :
#             break
#         elif numero % 2 == 0:
#             arqPar.write(f'{numero}\n')
#         else:
#             arqImpar.write(f'{numero}\n')
#     arqImpar.close()
#     arqPar.close()
# except ValueError as v:
#     print('Entre com um numero inteiro')
# except Exception as e:
#     print(e)

# xercício 5 — Faça um programa que abra os dois arquivos criados no exercício anterior e
# copie-os para um novo arquivo (
# numeros_ordenados.txt
# ), colocando-os em ordem
# crescente.

# try:
#     numeros, pares, impares = [], [], []
#     arqPar = open('pares.txt', 'r', encoding='utf-8')
#     arqImpar = open('impares.txt', 'r', encoding='utf-8')
#     numeros = [int(x) for x in arqPar.readlines() + arqImpar.readlines()]
#     # pares = arqPar.readlines()
#     # pares = [int(x) for x in pares]
#     # impares = arqImpar.readlines()
#     # impares = [int(x) for x in impares]
#     # numeros = pares+impares
#     numeros.sort()
#     print(numeros)
#     arqImpar.close()
#     arqPar.close()
# except FileNotFoundError:
#     print('Arquivo não encontrado')

# #6.Exercício 6 — O arquivo
# notas.txt
#  armazena, em cada linha, o RM, o nome e quatro notas
# de um aluno, separados por vírgula (
# RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
# ). Leia esse arquivo e
# calcule a média de cada aluno.
# frase = 'Hoje esta chovendo'
# palavras = frase.split()
# print(palavras)
#
# frase = 'Hoje,esta,chovendo'
# palavras = frase.split(',')
# print(palavras)


# try:
#     with open('notas.txt', 'r') as aNotas:
#         linhas = aNotas.readlines()
#         print(linhas)
#         for linha in linhas:
#             aluno = linha.strip().split(',')
#             #print(aluno)
#             #1a maneira
#             media = (float(aluno[2]) + float(aluno[3]) + float(aluno[4]) + float(aluno[5])) /4
#             #2a maneira
#             notas = [float(nota) for nota in aluno[2:]]
#             media = sum(notas) / 4
#
#             print(f'{aluno[1]} média: {media:.1f}')
# except FileNotFoundError:
#     print('Arquivo de notas')
# except Exception as erro:
#     print(erro)

#Exercício complementar 1 — O arquivo
# ips.txt
#  traz uma listagem de endereços IP que
# acessaram um site (um IP por linha, podendo haver repetidos). A partir desse arquivo, gere
# um novo arquivo
# ips_unicos.txt
#  com uma listagem de IPs únicos (sem valores repetidos).


# try:
#     ips = set()
#     with open('ips.txt', 'r') as aips:
#         for linha in aips.readlines():
#             ips.add(linha.strip())
#     ips = list(ips)
#     ips.sort()
#     print(ips)
#     with open('ipsunicos.txt', 'w') as aips:
#         aips.writelines([ip + '\n' for ip in ips])
# except FileNotFoundError:
#     print('Arquivo de ips nao encontrado')
# except Exception as erro:
#     print(erro)

ALIMENTO = 2
try:
    contagem_alimento = {}
    with (open('foods.txt', 'r') as aFoods):
        linhas = aFoods.readlines()
        print(linhas)
        for linha in linhas:
            pesquisa = linha.strip().split(',')
            contagem_alimento[pesquisa[ALIMENTO]] = \
            contagem_alimento.get(pesquisa[ALIMENTO], 0) + 1
    print(contagem_alimento)
    alimento_preferido = max(contagem_alimento, key=contagem_alimento.get)
    print(alimento_preferido)
except FileNotFoundError:
    print('Arquivo de foods nao encontrado')
except Exception as erro:
    print(erro)