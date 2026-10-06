


#Exercicio 1


import requests
import re
def remove_html(texto: str) -> str:
    return(re.sub(r'<[^>]+>', '', texto))

def get_info_teste(url:str):
    try:
        if url:
            resposta = requests.get(url, verify=False)
        if resposta.status_code == 200:
            dados = resposta.json()
            print(type(dados))
            print(dados)
        else:
            raise Exception (f"Erro de requisicao: {resposta.status_code}")

    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexao {e}")
    except Exception as e:
        print(e)

def get_municipios():
    try:
        uf = input('Digite a UF: ')
        resposta = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios', verify=False)
        municipios = []
        if resposta.status_code == 200:
            dados = resposta.json()
            #print(type(dados))
            #print(dados)
            for municipio in dados:
                municipios.append(municipio['nome'])
            print(municipios)
            print(f'Quantidade de municipios de {uf}: {len(municipios)}')
        else:
            raise Exception(f"Erro de requisicao: {resposta.status_code}")

    except requests.exceptions.ConnectionError as e:
        print("Erro de conexao")
    except Exception as e:
        print(e)

def get_pessoas():
    try:
        pessoas = []
        n = input('Digite a quantidade de pessoas: ')
        resposta = requests.get(f'http://randomuser.me/api/?results={n}', verify=False)

        if resposta.status_code == 200:
            dados = resposta.json()
            #print(type(dados))
            #print(dados)
            for pessoa in dados['results']:
                pessoas.append(pessoa['name']['first'] + ' ' + pessoa['name']['last'])
                pessoas.sort()
            print(pessoas)

        else:
            raise Exception(f"Erro de requisicao: {resposta.status_code}")

    except requests.exceptions.ConnectionError as e:
        print("Erro de conexao")
    except Exception as e:
        print(e)


def get_receitas():
    try:
        ingrediente = input('Digite o ingrediente procurado: ')
        resposta = requests.get(f'http://dummyjson.com/recipes?limit=50')

        if resposta.status_code == 200:
            dados = resposta.json()
            for receita in dados['recipes']:
                if ingrediente in receita['ingredients']:
                    print(receita['name'])
        else:
            raise Exception(f"Erro de requisicao: {resposta.status_code}")
    except requests.exceptions.ConnectionError as e:
        print("Erro de conexao")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # texto = """<body>
    #     <h1>Título Principal da Página</h1>
    #     <p>Este é um parágrafo comum de texto. Você pode usar <b>negrito</b> e <i>itálico</i> para destacar palavras.</p>
    #     <h2>Subtítulo da Seção</h2>
    #     <p>Este é o segundo parágrafo, separado do anterior por ocupar um novo bloco na tela.</p>
    # </body>"""
    # print(texto)
    #
    # print(remove_html(texto))

    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios'
    url2 = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/distritos'
    url3 = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    #get_info_teste(url3)
    #get_municipios()
    #get_pessoas()
    get_receitas()