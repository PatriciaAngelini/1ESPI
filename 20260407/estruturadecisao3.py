#Estrutura de Decisao
#Case
titulo = 'Dia da semana'
print(f'{titulo:^30}')
numero = int(input('Escolha um numero de 1 até 7: '))
#abordagem de match case
match numero:
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case 1 | 7: #equivale ao or
        print('Fim de semana')
    case _: #equivale ao else:
        print('Numero inválido')




#case