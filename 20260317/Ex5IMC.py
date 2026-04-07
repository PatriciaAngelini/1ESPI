print("IMC")
peso = float(input("Entre com seu peso em kilos: "))
altura = float(input("Entre com a sua altura em metros: "))
# quadrado = altura * altura
# imc = peso / quadrado
imc = peso / altura ** 2
#imc = round(peso / altura ** 2) #altera o imc permanentemente para 2 casas decimais
print('Com', peso, 'quilos e', altura, 'metros, você tem', round(imc, 2), 'de imc')