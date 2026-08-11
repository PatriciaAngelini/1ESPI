#Area do retangulo
def area_retangular(altura:float, largura:float) -> float:
    """
    Calcula a area de um retangulo
    :param altura: altura do retangulo
    :param largura: largura do retangulo
    :return: area do retangulo
    """
    if altura <= 0 or largura <= 0:
        #return 0
        raise ValueError('altura and largura deve ser positivo.')
    area = altura * largura
    return area

print(area_retangular(5, 4))
print(area_retangular(0, 4))