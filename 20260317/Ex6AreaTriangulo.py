print("Area Triangulo")
base = float(input('Entre com a base do triangulo em cm: '))
altura = float(input('Entre com a altura do triangulo em cm: '))
area = base * altura / 2
#print('A area do triângulo de base', base, 'e altura', altura, 'é igual a', area)
#como misturar frases + variaveis?
#função da f-string
print(f'A area do triângulo de base {base} e altura {altura} é igual a {area}')
print('A area do triângulo de base {} e altura {} é igual a {}'.format(base, altura, area))