"""
Faça um algoritmo que solicita ao usuário as notas de três provas.
Calcule a média aritmética e informe se o aluno foi Aprovado ou Reprovado
(o aluno é considerado aprovado com a média igual ou superior a 6).
"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'Aprovado com média {media:.2f}')
else:
    print(f'Reprovado com média {media:.2f}')
