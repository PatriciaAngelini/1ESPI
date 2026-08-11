def mostrar_informacoes(nome: str, idade: int, cidade: str) -> None:
    print(f'Nome: {nome} - Idade: {idade} (Cidade: {cidade})')

mostrar_informacoes('Angelica', 40, 'Adamantina')
mostrar_informacoes('Mateus', 40, '')

def mostrar_informacoes1(nome: str, idade: int, cidade: str = 'Nao informada') -> None:
    print(f'Nome: {nome} - Idade: {idade} (Cidade: {cidade})')
mostrar_informacoes1('Antonio', 40)

def mostrar_informacoes2(nome: str, idade: int, cidade: str = 'Nao informada') -> list[object]:
    return [nome, idade, cidade]
print(f'{mostrar_informacoes2('Juvenal', 40)}')
pessoa = mostrar_informacoes2('Juvenal', 40)
print(f'Nome: {pessoa[0]}, idade: {pessoa[1]}, cidade: {pessoa[2]}')