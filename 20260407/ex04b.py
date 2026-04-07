"""
Faça um algoritmo que solicita ao usuário uma letra e exiba uma mensagem informando se é uma
vogal ou uma consoante.
"""

letra = input('Digite uma letra: ')
vogais = 'aeiouAEIOU'
#if letra in ('a', 'e', 'i', 'o', 'u'):         # se a letra estiver contida na string de vogais
if letra in vogais:         # se a letra estiver contida na string de vogais
    print('Vogal')
else:
    print('Consoante')
