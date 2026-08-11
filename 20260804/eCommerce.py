#1a cadastrar produto
#paramentros: catalogo, nome do produto, valor, quantidade
#Exemplo depois e cadastrado
#[['Camiseta Azul', 89.90, 50], ['Cachecol', 35.00, 30]]
NOME = 0
PRECO = 1
ESTOQUE = 2

# catalogo = []
# def cadastrar_produto ():
#     nome = input("Digite o nome do produto: ")
#     preco = float(input("Digite o preco do produto: "))
#     estoque = int(input("Digite o estoque do produto: "))
#
#     produto = [nome, preco, estoque]
#     catalogo.append(produto)
# cadastrar_produto()
# cadastrar_produto()
# print(catalogo)


def cadastrar_produto(catalogo:list[list[object]],
                      nome:str, preco:float, estoque:int) -> list[list[object]]:
    """Cadastra um produto em um catalogo
    Params:
    :catalogo lista de produtos
    :nome nome do produto
    :preco preco do produto
    :estoque quantidade de estoque

    Returns: lista de produtos cadastrados"""

    catalogo.append([nome, preco, estoque])
    return catalogo

#2a funcao
#Exibir o que esta no catalogo
#Exemplo : Camiseta Azul - R$89.90 (estoque:50)



def exibir_catalogo(catalogo:list[list[object]]) -> None:
    for produto in catalogo:
        print(f'{produto[NOME]} - R${produto[PRECO]:.2f} (estoque:{produto[ESTOQUE]})')

loja = [['Camiseta Azul', 89.90, 50], ['Tenis Runner', 345.60, 80]]
exibir_catalogo(loja)

#Area de testes
# loja = []
# produto = input("Digite o nome do produto: ")
# valor = float(input("Digite o valor do produto: "))
# qtde = int(input("Digite o quantidade de produtos: "))
# cadastrar_produto(loja,produto,valor,qtde)

loja = [['Camiseta Azul', 89.90, 50], ['Tenis Runner', 345.60, 80]]
exibir_catalogo(loja)