#1
# def valida_cpf(cpf) -> int|bool:
#     # Remove caracteres não numéricos
#     cpf = ''.join(filter(str.isdigit, cpf))
#
#     # Verifica se tem 11 dígitos
#     if len(cpf) != 11:
#         return False
#
#     # Rejeita CPFs com números repetidos (ex: 111.111.111-11)
#     if cpf == cpf[0] * 11:
#         return False
#
#     # Cálculo do primeiro dígito verificador
#     soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
#     resto = (soma * 10) % 11
#     digito1 = 0 if resto == 10 else resto
#
#     # Cálculo do segundo dígito verificador
#     soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
#     resto = (soma * 10) % 11
#     digito2 = 0 if resto == 10 else resto
#
#     # Compara os dígitos calculados com os informados
#     if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
#         return int(cpf)
#     else:
#         return False
#
# pessoas = {}
# for _ in range(2):
#     cpf = input('digite seu CPF: ')
#     nome = input('digite seu nome: ')
#     if int(cpf) == valida_cpf(cpf):
#         pessoas[nome] = cpf
#     else:
#         print('digite um cpf valido')
#         pessoas.clear()
#         break
# print(pessoas)

# pessoas = {}
# for _ in range(2):
#     cpf = int(input('digite seu CPF: '))
#     nome = input('digite seu nome: ')
#     if len(str(cpf)) != 11:
#         print('digite um cpf valido')
#         pessoas.clear()
#         break
#     else:
#         pessoas[nome] = cpf
# print(pessoas)

# #2
# #cadastro
# produtos = {}
# for _ in range(5):
#     produto = input('produto: ')
#     valor = float(input(f'valor de {produto}: '))
#     produtos[produto] = valor
#
# #exibicao
# for produto, valor in produtos.items():
#     if valor > 50:
#         print(f'{produto}: R${valor:.2f}')

# #2 com dicionario com produtos maior que 50 separado
# produtos = {}
# for _ in range(5):
#     produto = input('produto: ')
#     valor = float(input(f'valor de {produto}: '))
#     produtos[produto] = valor
#
# #exibicao
# produtos_maior_50 = {}
# for produto, valor in produtos.items():
#     if valor > 50:
#         produtos_maior_50[produto] = valor
#
# print(produtos_maior_50)

# #3. notas de alunos
# alunos_notas = {}
# for _ in range(3):
#     rm = int(input('Entre com seu rm:'))
#     n1 = int(input('Entre com sua primeira nota:'))
#     n2 = int(input('Entre com sua segunda nota:'))
#     n3 = int(input('Entre com sua terceira nota:'))
#     notas = [n1, n2, n3]
#     alunos_notas[rm] = notas
#
# print(alunos_notas)
# for rm,notas in alunos_notas.items():
#     print(f'{rm} -> {sum(notas)/len(notas):.1f}')

#4. vogais
frase = input('Entre com uma frase: ')
a, e, i, o, u = 0, 0, 0, 0, 0
for letra in frase:
    match letra.lower():
        case 'a':
            a += 1
        case 'e':
            e += 1
        case 'i':
            i += 1
        case 'o':
            o += 1
        case 'u':
            u += 1
qtde_vogais = {'a':a, 'e':e, 'i':i, 'o':o, 'u':u}
print(qtde_vogais)