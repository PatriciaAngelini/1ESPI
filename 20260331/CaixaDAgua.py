titulo = "Caixa DAgua"
print(f'{titulo:^30}')

#numero par
bloco = int(input("Entre com o bloco de 1 a 4: "))
if bloco % 2 == 0 : #par
    print("Caixa A")
else:
    print("Caixa B")

bloco = int(input("Entre com o bloco de 1 a 4: "))
if bloco == 2 or bloco == 4 : #par
    print("Caixa A")
else:
    print("Caixa B")