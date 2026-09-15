#Muitas vezes precisar acessar o conteudo de um arquivo no file system
#Alguns tipos de arquivo o python le naturalmente, outros ele precisa de
#biblioteca especializada
#O arquivo texto é natural do python

print('Arquivo de Texto')
#para acessar um arquivo precisamos informar ao SO (sistema operacional)
#que vamos manipular o arquivo
#isso é feito através do OPEN / CLOSE
arqAlunos = open('alunos.txt', 'r')
#com o path completo
#arqAlunos = open('D:\\Projetos\\1ESPI\\20260915\\alunos.txt', 'r')
print('\nLendo e imprimindo uma linha do arquivo')
print(arqAlunos.readline())
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')

#o texto que eu estou lendo do arquivo é um elemento iteravel
print('\nLendo com o for')
for linha in arqAlunos:
    print(linha, end='')

#ao chegar no fim do arquivo, ele nao le e nao imprime mais nada
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')

#se eu quiser voltar e ler o arquivo desde o inicio
#tenho que voltar o cursor para o inicio
print('\nVolando para o inicio do arquivo')
arqAlunos.seek(0)
print(arqAlunos.readline(), end='')

print('\nLendo como uma lista de linhas')
listaLinhas = arqAlunos.readlines()
print(listaLinhas)

#desafio: usando list comprehension tirar  '\n' dos elementos da lista
listaLinhas = [linha.strip() for linha in listaLinhas]
print(listaLinhas)

listaLinhas = [linha.replace('\n', '') for linha in listaLinhas]
print(listaLinhas)


print('\nVoltando para uma posicao qq do arquivo arquivo')
arqAlunos.seek(15)
print(arqAlunos.readline(), end='')

print('\nLendo o arquivo todo') #muito cuidado com arquivos grandes
print(arqAlunos.read())

print('\nFechando arquivo')
arqAlunos.close()

print('\nEscrevendo um arquivo')
arqOlaMundo = open('arquivoOlaMundo.txt', 'w')
arqOlaMundo.write('Ola Mundo')
arqOlaMundo.close()

#o modo w sobrescreve o arquivo
arqOlaMundo = open('arquivoOlaMundo.txt', 'w')
arqOlaMundo.write('Bom dia mundo')
#ele gruda as linhas!!! como resolver isso?
arqOlaMundo.write('O dia esta maravilhoso')
arqOlaMundo.write('\n\n')
arqOlaMundo.write('Pulou a linha')
arqOlaMundo.close()

floricultura = ['rosa', 'gardenia', 'artemisia']
floricultura = [flor + '\n' for flor in floricultura]
arqFloricultura = open('arquivoFloricultura.txt', 'w')
arqFloricultura.writelines(floricultura)
arqFloricultura.close()



