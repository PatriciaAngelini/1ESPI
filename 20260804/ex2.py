#definindo a funcao
def dobro(valor:int) -> int:
    """
    Funcao que retorna o valor do dobro do valor
    :param valor: o valor que sera dobrado
    :return: o dobro do valor
    """
    return valor * 2

#usar a funcao
print(f'Dobro do valor: {6}')
help(dobro)