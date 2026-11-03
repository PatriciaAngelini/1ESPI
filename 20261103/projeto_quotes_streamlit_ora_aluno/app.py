import streamlit as st
from conexao_ora_aluno import conectar_oracle

#vamos deixar os selects na variavel global

SQL_TODAS_CITACOES = """
    SELECT quote_text, author_name FROM quotes
"""

SQL_AUTHOR = """
    SELECT quote_text, author_name FROM quotes 
    WHERE UPPER(author_name) LIKE UPPER(:1)
    ORDER BY quote_text ASC
"""

SQL_CITACAO = """
    SELECT quote_text, author_name FROM quotes 
    WHERE UPPER(quote_text) LIKE UPPER(:1)
    ORDER BY author_name ASC, quote_text ASC
"""

def consultar(sql, termo):
    conn = conectar_oracle()
    cursor = conn.cursor()
    if termo:
        cursor.execute(sql, (f'%{termo}%',))
    else:
        cursor.execute(sql)
    linhas = cursor.fetchall()
    cursor.close()
    conn.close()
    # dados = [{"Citação": "Frase A", "Autor": "Ana"},
    #          {"Citação": "Frase B", "Autor": "Bruno"}]
    dados = [{"Citação": c, "Autor": a} for c, a in linhas]
    #print(dados)
    return dados

def mostrar(dados):
    if not dados:
        st.info("Nenhum dado encontrado")
    else:
        st.caption(f"Encontradas {len(dados)} citacoes")
        st.dataframe(dados)



if __name__ == "__main__":
    if "pagina" not in st.session_state:
        st.session_state.pagina = "Todas Citacoes"

    st.sidebar.title("Menu")
    if st.sidebar.button("Todas Citacoes", width="stretch"):
        st.session_state.pagina = "Todas Citacoes"
    if st.sidebar.button("Buscar por Autor", width="stretch"):
        st.session_state.pagina = "Buscar por Autor"
    if st.sidebar.button("Buscar por Citacao", width="stretch"):
        st.session_state.pagina = "Buscar por Citacao"

    st.title("Pesquisa de Citações")

    if st.session_state.pagina == "Todas Citacoes":
        st.header("Todas Citações")
        dados = consultar(SQL_TODAS_CITACOES, "")
        mostrar(dados)

    if st.session_state.pagina == "Buscar por Autor":
        st.header("Busca por Autor")
        author = st.text_input("Nome (ou parte) do Autor")
        if author:
            dados = consultar(SQL_AUTHOR, author)
            mostrar(dados)

    if st.session_state.pagina == "Buscar por Citacao":
        st.header("Busca por Citacao")
        citacao = st.text_input("Nome (ou parte) da Citacao")
        if citacao:
            dados = consultar(SQL_CITACAO, citacao)
            mostrar(dados)