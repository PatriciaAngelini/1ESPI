from faker import Faker
import Funcoes
fake = Faker('pt-BR')

nome =  fake.name()
#print(nome)
print(Funcoes.Saudacao(nome))