#String se comporta como se fosse uma lista
#Sao uma sequencia de caracteres

frase = 'Eu amo Python'
print(frase)
lista = frase.split()
print(lista)

primeira_palavra = lista[0]
print(primeira_palavra)
letra = primeira_palavra[0]
print(letra)

frase = 'Eu amo Python'
print('\nImprimindo palavra a palavra')
for palavra in frase.split():
    print(palavra)

print('\nImprimindo letra a letra')
for letra in frase:
    print(letra)

if 'Python' in frase:
    print('Tem Python na frase')

print('\nSlicing de uma frase - dividindo em palavras')
frase = 'Eu amo Python'
lista_palavras = frase.split()
print(lista_palavras)
amor = lista_palavras[0:2]
print(amor)

print('\nSlicing de uma frase - dividindo em letras')
indices= '0123456789123'
frase =  'Eu amo Python'
print(frase[0:2])
print(frase[0:6])
print(frase[:6]) # nao importa o inicio quero ir ate o 6
print(frase[7:]) # vai do 7 ate  o fim
print(frase[-1:0:-1]) #come o E final
print(frase[::-1]) #o -1 inverte
print(frase[-1:-3:-1]) #os dois ultimos caracteres


