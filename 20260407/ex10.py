"""
Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor de uma
empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00
mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.
"""

salario_fixo = float(input('Salario Fixo: '))
valor_vendas = float(input('Valor Das Vendas: '))

if valor_vendas <= 1500:
    comissao = valor_vendas * 3 / 100
    total = salario_fixo + comissao
else:
    valor_a_mais = valor_vendas - 1500
    comissao1 = 1500 * 3 / 100
    comissao2 = valor_a_mais * 5 / 100
    total = salario_fixo + comissao1 + comissao2

print(f'Total: {total:.2f}')
