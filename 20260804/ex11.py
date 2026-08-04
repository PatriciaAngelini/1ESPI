def soma_divisores(numero:int)->int:
    """
    Soma os divisores de um numero inteiro
    :param numero: numero a ser calculado
    :return: soma dos divisores
    """
    soma=0
    for num in range(1,numero+1):
        if numero % num==0:
            soma+=num
    return soma

print(soma_divisores(6))