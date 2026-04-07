#Estrutura de Decisao
#if, then(:), else:
#igualdades (==) e desigualades (>, <, >=, <=, !=)
#operadores logicos - juntam duas ou mais comparacoes no mesmo if
#and (malvado), or (bonzinho), not (do contra)
#elif
#nada mais é que a junção do else+if
titulo = 'Dia da semana'
print(f'{titulo:^30}')
numero = int(input('Escolha um numero de 1 até 7: '))
#abordagem de ifs aninhados
if numero == 5: #como estamos comparando com igualdades
    #tanto faz comparar com o 1(domingo) primeiro
    #como com o 5(quinta)
    #é particularmente interessante usar o numero mais escolhido
    #na primeira comparacao, para priorizar performance
    print('Quinta-feira')
else:
    if numero == 2:
        print('Segunda-feira')
    else:
        if numero == 3:
            print('Terça-feira')
        else:
            if numero == 4:
                print('Quarta-feira')
            else:
                if numero == 1:
                    print('Domingo')
                else:
                    if numero == 6:
                        print('Sexta-feira')
                    else:
                        if numero == 7:
                            print('Sabado')
                        else:
                            print('Numero inválido')




#case