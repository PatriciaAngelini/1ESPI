"""
Faça um algoritmo que solicita ao usuário uma letra e exiba uma mensagem informando se é uma
vogal ou uma consoante.
"""

letra = input('Digite uma letra: ').lower()         # lower() converte uma string para minúsculo
#if letra == 'a' or 'e' or 'i': ERRADO
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Vogal')
else:
    print('Consoante')
