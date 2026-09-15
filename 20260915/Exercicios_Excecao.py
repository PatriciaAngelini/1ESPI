# Exercício 1 Leia um número inteiro digitado pelo usuário e imprima o seu quadrado (o número elevado
# ao quadrado). Trate # ValueError #  caso o valor informado não seja um número inteiro.
# try:
#     numero = int(input('Entre com um numero: ')) # --> se for float ja cai no erro
#     # if type(numero) is not int:                  --> nao preciso fazer isso pq
#     #     raise ValueError('Valor não é inteiro')  --> ao tentar converter para int ja da erro
#     print(f'O quadrado do numero: {numero**2}')
# except ValueError as ve:
#     print(f'Valor invalido: {ve}')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')


# Exercício 2 Elabore um algoritmo que leia dois números e imprima qual é o maior e qual é o menor. Se
# eles forem iguais, lance uma exceção explicando o motivo e trate essa exceção, encerrando a
# comparação de forma controlada (sem travar o programa).
# try:
#     numero1 = int(input('Entre com um numero: '))
#     numero2 = int(input('Entre com outro numero: '))
#     if numero1 == numero2:
#         raise ValueError('Numeros Iguais')
#     elif numero1 > numero2:
#         print(f'{numero1} > {numero2}')
#     else:
#         print(f'{numero2} > {numero1}')
# except ValueError as ve:
#     print(f'Valor invalido: {ve}')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')


# Exercício 3 Elabore um algoritmo que leia uma letra entre A, B, C ou D
# e imprima o nome de uma fruta
# que comece com essa letra.
# Caso seja digitada qualquer outra letra, deverá ser lançada uma exceção.
# frutas = {
#     'a': 'abacaxi',
#     'b': 'banana',
#     'c': 'caqui',
#     'd': 'damasco'
# }
# try:
#     letra = input('Digite uma letra: ').lower().strip()
#     if letra not in frutas:
#         raise ValueError('Letra invalida')
#     else:
#         print(f'{frutas[letra]}')
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)


# Exercício 4 Para vários tributos, a base de cálculo é o salário mínimo.
# Elabore um algoritmo que leia o
# valor do salário mínimo e o valor do salário de uma pessoa.
# Calcule e imprima quantos salários
# mínimos essa pessoa ganha. Lance tratamentos de exceção condizentes
# (entrada inválida, salário
# mínimo negativo e divisão por zero).
# salario_minimo = 1621
# try:
#     salario = float(input('Entre com o seu salario: '))
#     if salario < 0 or salario_minimo < 0:
#         raise ValueError('Negativo')
#     else:
#         print(f'Você ganha {salario/salario_minimo:.2f} salarios minimos')
# except ValueError as v:
#     print(f'Valor invalido: {v}')
# except ZeroDivisionError:
#     print('Divisao por zero')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')


# Exercício 5 Escreva uma função
# buscar_item_por_indice(lista: list[str], indice: int) -> str
#  que retorna o item de uma lista na posição informada.
#  Em seguida, leia um índice digitado pelo usuário e
# mostre o produto correspondente em uma lista de produtos em promoção, tratando
# IndexError# (posição que não existe) e  ValueError (índice que não é um número inteiro).
# def buscar_item_por_indice(lista: list[str], indice: int) -> str
#     print(f'Buscando o indice {indice}')
#     return lista[indice]
# promocao=['calca', 'celular', 'ceroula']
# try:
#     indice = int(input('Insira um valor: '))
#     print(f'Item em promocao: {buscar_item_por_indice(promocao, indice)}')
# except IndexError:
#     print('Indice invalido')
# except ValueError:
#     print('Valor invalido')


# Exercício 6 Crie um dicionário com o preço de alguns produtos (nome do produto -> preço). Peça ao
# usuário o nome de um produto e imprima o preço correspondente. Trate KeyError
#  caso o produto não esteja cadastrado no dicionário.
produtos = {
    "Camiseta" : 50.00,
    "Tenis Runner": 120.00,
    "Boné Preto": 70.00
}
try:
    produto = input('Pesquise o valor de um produto: ')
    print(f'O preco do {produto} é R${produtos[produto]:.2f}')
except KeyError:
    print('Produto inexistente')

# Exercício 7 Peça dois números ao usuário e calcule a média entre eles. Use uma cláusula
# else para exibir uma mensagem de sucesso somente quando o cálculo for bem-sucedido,
# e uma cláusula
# finally para exibir sempre a mensagem "Cálculo finalizado.", tenha ocorrido erro ou não. Trate
# ValueError na conversão dos números.

try:
    n1 = float(input('Primeiro numero: '))
    n2 = float(input('Segundo numero: '))
except ValueError:
    print('Valor invalido')
except Exception as e:
    print('Ocorreu um erro')
else:
    print(f'A media entre {n1} e {n2} foi de {(n1+n2)/2:.2f}')
finally:
    print('Calculo Finalizado')

# Exercício 8 (nível avançado) Leia o nome de um produto,
# a quantidade disponível em estoque e a
# quantidade que um cliente deseja comprar.
# Se a quantidade desejada for maior que o estoque
# disponível, lance um ValueError explicando o problema.
# Separe a leitura dos dados (que pode gerar erro de conversão)
# da validação de negócio (estoque insuficiente) usando dois blocos
# try
#  — um
# para cada situação — e apelidos (
# as
# ) diferentes e descritivos para cada exceção, seguindo a boa
# prática vista na seção 1.9.

#Arthur
# EX8

lista_de_produtos = {
    ("Mouse", 10),
    ("Teclado", 15),
    ("Monitor", 6),
    ("MousePad", 2),
}
print("\n")
print(lista_de_produtos)
try:
    pedido = str(input("Digite o nome do produto que deseja: "))
    qtde_pedido = int(input(f"Digite a quantidade de {pedido} que deseja: "))

except ValueError as erro_leitura:
    print(f"Erro na leitura dos dados: ({erro_leitura})")
else:
    try:
        for produto, estoque in lista_de_produtos:
            if produto.lower() == pedido.lower():
                if qtde_pedido > estoque:
                    raise ValueError(f"Estoque insuficiente! Temos apenas {estoque} unidade(s) de {produto}.")
                else:
                    print(f"Pedido realizado com sucesso! Produto: {produto} | Quantidade: {qtde_pedido}")

    except ValueError as erro_estoque:
        print(f"Erro na validação do estoque: ({erro_estoque})")