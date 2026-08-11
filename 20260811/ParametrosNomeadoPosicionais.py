#Funcoes: outros temas

#Parametros nomeados e posicionais

def calcular_media (python:float, webdev:float, frontend:float) ->float:
    """
    Calcula a media de python, webdev, frontend
    :param python: nota de python
    :param webdev: nota de webdev
    :param frontend: nota de frontend
    :returns: media de python, webdev, frontend
    """
    return (python + webdev + frontend) / 3

#durante o uso definimos se a passagem de parametro sera nomeada ou posiciona
media = calcular_media(9, 8, 9.5)
#racional posicional
#1 posicao a nota 9 se refere a nota de python
#2 posicao a note se refere ao webdev
#3 posicao a nota se refere a frontend
print(f'Media: {media:.1f}')

#parametros nomeados
media = calcular_media(webdev=9, frontend=7, python= 9.5)
print(f'Media: {media:.1f}')

#cuidado com a mistura
#nao funciona parametro nomeado na frente de posicional
# media = calcular_media(python= 9.5, 8, 7)
# print(f'Media: {media:.1f}')

#funciona parametro posicional na frente de nomeado
media = calcular_media(9.5, 8, frontend=7)
print(f'Media: {media:.1f}')