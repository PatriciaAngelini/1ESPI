#Excecoes parte 2
#Sao erros que acontecem no tempo de execucao de um programa

print('Exceções')
print('\nTicket medio supermercado - com lancamento de exceçao')
#lancamos exceção quando do ponto de vista do negocio aquela operacao esta errada
#nesse caso do exemplo, qdo temos um valor negativo de compras ou de quantidade

try:
    valor = float(input('Digite um valor gasto na compra: '))
    qtde = int(input('Digite a quantidade de itens da compra: '))
    if valor < 0 or qtde < 0:
        #raise Exception('Valor ou Quantidade negativo') #lançando exceção
        raise ValueError('Valor ou Quantidade negativo')
    ticket_medio = valor / qtde
except ValueError as v:
    print(f'Valor invalido:{v}')
except Exception as e:
    print(f'Ocorreu um erro, contate o administrador: {e}')
else: #só executa qdo não ha err
    print(f'O seu ticket medio é R${ticket_medio:.2f}')
finally: #sempre é executado
    print('Obrigada por comprar no supermercado BEM BARATO')