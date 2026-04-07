"""
Resumo da PEP 8 (Guia de Estilo do Python)

📁 Nomeação de arquivos:
- Use letras minúsculas
- Separe palavras com underscore (_)
- Evite espaços e caracteres especiais

Exemplos:
- correto: calculadora_media.py
- correto: usuario_service.py
- errado: Calculadora.py
- errado: meu arquivo.py

🏷️ Convenções de nomes:

snake_case:
- Todas as letras minúsculas
- Palavras separadas por underscore (_)
- Usado para variáveis, funções e arquivos

Exemplos:
- nome_usuario
- calcular_media
- total_itens

PascalCase:
- Cada palavra começa com letra maiúscula
- Sem separadores entre palavras
- Usado para nomes de classes

Exemplos:
- Pessoa
- CalculadoraFinanceira
- UsuarioService
"""

# 📦 IMPORTS (devem ficar no topo do arquivo e organizados)
import os
from math import sqrt

# 🏷️ CONSTANTES (nomes em MAIÚSCULAS)
PI = 3.14


# 🧱 IDENTAÇÃO
# Use 4 espaços por nível (nunca use tab)
def exemplo_identacao():
    print("Indentação correta com 4 espaços")


# 🏷️ NOMEAÇÃO

# Variáveis e funções → snake_case
idade_usuario = 25


def calcular_media(valores):
    # 🧠 Espaços em branco
    # Use espaços ao redor de operadores para melhorar leitura
    soma = sum(valores)
    total = len(valores)

    # 🔍 Comparações
    # Prefira "is None" ao invés de "== None"
    if total is None or total == 0:
        return 0

    return soma / total


# Classes → PascalCase
class Pessoa:
    def __init__(self, nome):
        self.nome = nome


# 📏 TAMANHO DA LINHA
# Evite linhas com mais de 79 caracteres
mensagem = "Essa é uma linha dentro do limite recomendado"

# 📐 QUEBRA DE LINHA
# Use parênteses para quebrar linhas longas
resultado = (
        10 + 20 + 30
)

# 🔤 STRINGS
# Use aspas simples ou duplas com consistência
nome = "Maria"


# 🧾 COMENTÁRIOS
# Use comentários para explicar o PORQUÊ, não o óbvio

# Exemplo de função simples bem escrita
def calcular_soma(x, y):
    return x + y


# ❌ Evite código difícil de ler:
# def calc(x,y):return x+y

# ✅ Prefira código claro e legível:
def calcular_soma_melhor(x, y):
    return x + y


# 🧪 BOAS PRÁTICAS GERAIS
# - Use nomes descritivos
# - Evite funções muito grandes
# - Separe responsabilidades

if __name__ == "__main__":
    exemplo_identacao()
    media = calcular_media([10, 20, 30])
    print("Média:", media)