#Consumo API

#Api serve para recuperarmos dados a partir da chamada de um progrma
#Tipicamente esses "programas" estao disponiveis em alguma url

## nossa aplicacao --> requisicao para um servidor (API)
## nossa aplicacao <-- resposta

#Requisicoes sao feitas atraves do REQUEST
#Quando usamos http usamos a biblioteca requests
#pip install requests
#dinamica
#para fazer a requisicao usamos requests.get
#e recebemos a resposta com resposta.json

#tb temos o status a resposta
#resposta.status_code --> 200 ok, 404 file not found, 500 internal error

import requests
def get_informacoes_localidade():
    try:
        cep = input('Digite o CEP com 8 digitos: ')
        resposta = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
        if resposta.status_code == 200:
            dados = resposta.json()
    #        print(type(dados))
    #        print(dados)
            print(f'logradouro: {dados["logradouro"]}')
            print(f'complemento: {dados["complemento"]}')
            print(f'bairro: {dados["bairro"]}')
            print(f'localidade: {dados["localidade"]}')
            print(f'uf: {dados["uf"]}')
        else:
            raise Exception (f"Erro de requisicao: {resposta.status_code}")

    except requests.exceptions.ConnectionError as e:
        print("Erro de conexao")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    get_informacoes_localidade()



