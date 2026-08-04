#Reajuste condicional
def reajuste_condicional(salario:float) -> float:
    """
    Reajusta o salario  condicionalmenta
        se maior que 2000 reajusta em 7%
        caso contrario reajusta em 15%
    :param salario: salario atual
    :return: salario reajustado
    """
    if salario > 2000:
        return salario * 1.07
    else:
        return salario * 1.15


salario_atual = float(input('Entre com seu salario atual: '))
print(f'R${reajuste_condicional(salario_atual):.2f}')