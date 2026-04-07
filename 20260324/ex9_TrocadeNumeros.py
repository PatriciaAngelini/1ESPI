print('Troca de Numeros')
A = int(input('Entre com um numero: '))
B = int(input('Entre com outro numero: '))
print(f'A:{A} e B:{B}')
#salvando o valor de A
TEMP = A
#sobreescrevendo o A
A = B
B = TEMP
print(f'A:{A} e B:{B}')

#Outro jeito de fazer
A = int(input('Entre com um numero: '))
B = int(input('Entre com outro numero: '))
print(f'A:{A} e B:{B}')
A, B = B, A
print(f'A:{A} e B:{B}')