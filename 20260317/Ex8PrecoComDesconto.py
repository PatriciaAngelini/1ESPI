print("Preço com desconto")
d=0.1 #10% de desconto => constante
amarelo = '\033[1;93m'
reset = '\033[0;0m'
vermelho = '\033[1;31m'

preco = float(input('Informe o preço: '))
precocomdesconto = preco * (1-d)
print(f'Preco cheio:R${amarelo}{round(preco,2)}{reset}'
      f'\nPreco com desconto:R${vermelho}{round(precocomdesconto,2)}{reset}')
