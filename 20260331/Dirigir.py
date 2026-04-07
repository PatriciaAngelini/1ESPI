titulo = "Dirigir"
print(f'{titulo:^30}')
idade = int(input("Que idade você tem?: "))
cnh = input("Você tem CNH")
#Operadores RELACIONAIS
#São os que vão combinar as comparações
#AND é o operador MALVADO, só deixa prosseguir se tudo for SIM
#OR é o operador BONZINHO, qualquer um que for SIM ele deixa prosseguir
#NOT é do CONTRA, ele faz tudo ao contrario

if idade >= 18 and cnh == 'sim':
    print("Você pode dirigir")
else:
    print("Não pode dirigir")
print("TRANSITO DE SAO PAULO AGRADECE")