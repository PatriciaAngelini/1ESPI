titulo = 'Vogais'
print(f'{titulo:^20}')
letra = input('Entre com uma letra: ').lower() #transforma em minuscula
if letra not in '0123456789':
    match letra:
        case 'a'|'e'|'i'|'o'|'u':
            print('vogal')
        case _:
            print('consoante')
else:
    print('É um numero')