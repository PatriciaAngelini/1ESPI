"""Gerar uma matriz 4 X 3 que armazene nomes aletorios"""
import faker
#instanciando o objeto
pessoa = faker.Faker('pt-BR')
#print(pessoa.name())
matriz = []
for linha in range(4):
    pessoas = []
    for coluna in range(3):
        pessoas.append(pessoa.name())
    matriz.append(pessoas)
print(matriz)