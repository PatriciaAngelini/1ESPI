"""
Peca para o usuario fornecer dois numeros e uma opcao
A opcao 1 é soma, 2 subtração, 3 multiplicacao, 4 divisao
"""
titulo = "Operacoe Matematicas"
print(f'{titulo:^30}')
n1 = float(input('Entre com um numero: '))
n2 = float(input('Entre com outro numero: '))
# print("1-adição")
# print("2-subtração")
# print("3-multiplicação")
# print("4-divisão")

print("""
Escolha uma das operações
    1-adição
    2-subtração
    3-multiplicação
    4-divisão
""")

opcao = int(input('Opção: '))
match opcao:
    case 1:
        print(f'Adicão: {n1+n2:.2f}')
    case 2:
        print(f'Subtração: {n1 - n2:.2f}')
    case 3:
        print(f'Multiplicação: {n1 * n2:.2f}')
    case 4:
        print(f'Divisão: {n1 / n2:.2f}')
    case _:
        print('Opção Invalida')
# if 1 <= opcao <= 4:
# else:
#     print('Opção Invalida')




