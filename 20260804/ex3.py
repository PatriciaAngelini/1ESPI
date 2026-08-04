#definicao
def calcular_media(notas:list[float]) -> float:
    """
        Calcula media das notas

        :param notas:lista de notas
        :return: média de notas
    """
    #return sum(notas) / len(notas)

    total = 0.0
    for nota in notas:
        total += nota
    media = total / len(notas)
    return round(media, 1)

#uso
print(f'Minha Media:{calcular_media([8, 9.2, 9])}')