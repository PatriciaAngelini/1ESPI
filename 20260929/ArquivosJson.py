#json
#Pra tratar arquivos json o python tem uma biblioteca propria
#json

#Arquivos JSON são textos estrururados
print('Json')
pessoa = {'nome':'Patricia', 'idade':25, 'hobbies':['caminhada', 'tenis']}
print(type(pessoa))
print(pessoa)

#a biblioteca json vai pegar esse dicionario e transformar num texto
#porque é interessante? porque na hora de gravar um arquivo, nós precisamos de texto

import json
#o metodo dumps, da biblioteca json converte uma colecao em um texto
#dumps (onde o s é de string)
pessoa2 = json.dumps(pessoa)
print(type(pessoa2))
print(pessoa2)

#o uso mais comum, no entanto é gravar essas informações em um arquivo
#o metodo agora muda de nome: dump

with open('alunos1.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(pessoa, arqAlunos)


with open('alunos2.json', 'a', encoding='utf-8') as arqAlunos:
    json.dump(pessoa, arqAlunos,indent=4)


print('\nAcentuação')
#acentuacao
pessoanova = {'nome':'João Àlvarez', 'idade':43, 'hobbies':['caçada de formiga', 'tênis']}
print('Sem o parametro ensure_ascii')
pessoanova2 = json.dumps(pessoanova,indent=4)
print(type(pessoanova2))
print(pessoanova2)
print('Com o parametro ensure_ascii')
pessoanova2 = json.dumps(pessoanova,indent=4,ensure_ascii=False)
print(type(pessoanova2))
print(pessoanova2)

with open('alunos3.json', 'a', encoding='utf-8') as arqAlunos:
    json.dump(pessoanova, arqAlunos,indent=4,ensure_ascii=False)

alunos = {
    139219884:{'nome': 'Patricia', 'idade': 25, 'hobbies': ['caminhada', 'tenis']},
    467478856:{'nome':'João Àlvarez', 'idade':43, 'hobbies':['caçada de formiga', 'tênis']}
}

with open('todosalunos.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(alunos, arqAlunos,indent=4,ensure_ascii=False)

print('\n\nLeitura JSON')
#enquanto o dumps(string)/dump(arquivo) escreve no formato JSON
#o loads(string)/load(arquivo) le do formato JSON e coloca numa colecao

pessoatexto = '{"nome":"Antonio", "idade":25, "hobbies":["aeromodelismo", "board games"]}'
print(type(pessoatexto))
print(pessoatexto)
#o metodo LOADS tranforma essa string em uma colecao
pessoadicionario = json.loads(pessoatexto)
print(type(pessoadicionario))
print(pessoadicionario)

#como ler de um arquivo? metodo LOAD
with open('alunos1.json', 'r', encoding='utf-8') as arqAluno:
    aluno = json.load(arqAluno)
    print(type(aluno))
    print(aluno)







