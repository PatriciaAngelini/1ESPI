#Python tem tipagem dinamica

x = 10
print(type(x))
nome = 'Paulo'
print(type(nome))

#Type Hints ajuda a definir o tipo de dados esperado na variavel
#mas é apenas uma AJUDA, ou seja o python não impede que seja atribuido
#um valor com outro tipo de dados.

nome: str = 'Paulo'
print(type(nome))

nome = 123
print(type(nome))

preco: float
preco = 7.8
print(type(preco))

#todos os tipos de dados são aceitos no type hints
#int, float, bool, str, list, etc
disponivel: bool = True
print(type(disponivel))

#o tipo de uso mais importante é quando definimos funcoes
#quando definimos o tipo de dados esperado como parametro e tambem o tipo
#de dados de retorno da funçao, estamos definindo a
# ASSINATURA da funcao
# isso é importante para disponibilizarmos essas funcoes, por exemplo,
# como API

def calcular_total(preco: float, quantidade:int) -> float:
    return preco * quantidade

print(calcular_total(preco, 2))
print(calcular_total(preco, 3))

# e quando a funcao nao tem retorno?
# usamos o None
def exibir_produto(produto: str, preco: float) -> None:
    print(f"{produto} - {preco}")

#exibir_produto('Leite', 8.9)
exibir_produto('Leite', 8.9)

#revisao de list
#--> tipo de dados composto
minhaLista:list = ['cafe', 'chantilly', 'biscoito']
print(minhaLista)

dadosPessoais = ['Patricia', 54, 'feminino', 'superior']
print(dadosPessoais)
print(f"Nome: {dadosPessoais[0]}")
print(f"Idade: {dadosPessoais[1]}")
dadosPessoais.append('Professor')
print(dadosPessoais)
print("\nImprimindo a lista elemento a elemento")
for item in dadosPessoais:
    print(item)


#mas e o tipo list???
#vamos aplicar a lista usando type hint em funcoes
def somar_precos(precos: list) -> float:
    total: float = 0
    #fale que o total é um float sem falar que é um float
    #total = 0.0
    for preco in precos:
        total += preco
    return total
print('\nSomando precos ')
print(f'total: {somar_precos([10, 20, 30])}')
#print(preco)
def criar_produto(produto: str, preco: float, quantidade: int) -> list:
    return [produto, preco, quantidade]
print(f'\nCriar Estoque')
print(f'Estoque: {criar_produto('Leite', 8.9, 10)}')

#tipo de dados generico: object
#quando usar -> na assinatura da funcao
#entendimento
#aqui estou criando uma lista que só aceita inteiros
idades: list[int] = [17, 54, 23]
print(f'Idades: {idades}')

#mas se eu quisesse uma lista mista?
produto = ['camisa', 29.9, 8]
print(f'Produto: {produto}')
#eu poderia lançar mão do objeto generico OBJECT
produto: list[object] = ['camisa', 29.9, 8]


#DOCSTRING
#documenta a funcao
def calcular_total(preco: float, quantidade: int) -> float:
    """Calcula a quantidade total de um produto

    Params:
        preco: preco unitario do produto
        quantidade: quantidade total de um produto

    Returns:
        total: preco total (preco*quantidade)

    """
    return preco * quantidade

help(calcular_total)