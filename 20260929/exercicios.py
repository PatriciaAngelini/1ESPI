import json
alunos ={}
with open('notas.txt', 'r', encoding='utf-8') as arqAlunos:
    for linha in arqAlunos:
        linha = linha.strip()
        aluno = linha.split(',')
        #print(aluno)
        rm = aluno[0]
        nome = aluno[1]
        notas_str = aluno[2:]
        notas = [float(nota) for nota in notas_str]
        print(rm, nome, notas)
        alunos[rm] = {'nome': nome, 'notas': notas}

print(alunos)
with open('notas.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(alunos, arqAlunos, indent=4, ensure_ascii=False)