base = 90
altura = 60
area = base * altura / 2
#função da f-string
print(f'Base {base} altura {altura} e {area}')
#.format
print('Base {} altura {} e {}'.format(base, altura, area))

#Mudando a cor da area para vermelho
print(f'Base {base} altura {altura} e \033[1;31m{area}\033[0;0m')
print('teste')
texto = 'Meu carro é \033[1;31mvermelho\033[0;0m,\nnão uso \033[1;94mespelho\033[0;0m para me pentear'
print(texto)
reset = '\033[0;0m'
vermelho = '\033[1;31m'
azul = '\033[1;94m'
poema = f'\nDe tudo ao meu {vermelho}amor{reset} serei {azul}atento{reset}'
print(poema)


#cores ansi em python
# Cor	Fonte	Fundo
# Preto	\033[1;30m	\033[1;40m
# Vermelho	\033[1;31m	\033[1;41m
# Verde	\033[1;32m	\033[1;42m
# Amarelo	\033[1;33m	\033[1;43m
# Azul	\033[1;34m	\033[1;44m
# Magenta	\033[1;35m	\033[1;45m
# Cyan	\033[1;36m	\033[1;46m
# Cinza Claro	\033[1;37m	\033[1;47m
# Cinza Escuro	\033[1;90m	\033[1;100m
# Vermelho Claro	\033[1;91m	\033[1;101m
# Verde Claro	\033[1;92m	\033[1;102m
# Amarelo Claro	\033[1;93m	\033[1;103m
# Azul Claro	\033[1;94m	\033[1;104m
# Magenta Claro	\033[1;95m	\033[1;105m
# Cyan Claro	\033[1;96m	\033[1;106m
# Branco	\033[1;97m	\033[1;107m
# Negrito	\033[;1m	-
# Inverte	\033[;7m	-
# Reset (remove formatação)	\033[0;0m	-