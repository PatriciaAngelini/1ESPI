import oracledb
def conectar_oracle():
    user = "PF1076"
    dsn = "oracle.fiap.com.br:1521/orcl"
    password = input("Informe o seu senha: ")
    try:
        conn = oracledb.connect(user=user, dsn=dsn, password=password)
        print("Conexao estabelecida com sucesso!")
        return conn
    except oracledb.DatabaseError as e:
        (erro,) = e.args
        print(f"Erro ao conectar ao oracle:{erro.message}")
        return None

def testar_conexao():
    conn = conectar_oracle()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sysdate FROM dual") #faz a consulta
        resultado = cursor.fetchone() #recupera uma linha no formato de tupla
        #tupla é a irma da lista que não muda de tamanho, nem de items
        print(f'Teste ok: {resultado[0]}')
        cursor.close() #fechando a linha
        conn.close()

if __name__ == "__main__":
    print('Teste')
    testar_conexao()