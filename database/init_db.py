import os
import psycopg2

# Caminho absoluto para o arquivo create_tables.sql
sql_file_path = os.path.join(os.path.dirname(__file__), 'create_tables.sql')

# Obtendo a URL de conexão do banco de dados a partir das variáveis de ambiente
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não está definida.")

# Lendo o conteúdo do arquivo SQL
with open(sql_file_path, 'r') as file:
    sql_commands = file.read()

# Conectando ao banco de dados e executando o script SQL
try:
    # Estabelecendo a conexão
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    # Executando os comandos SQL
    cur.execute(sql_commands)
    
    # Confirmando as alterações
    conn.commit()
    print("Tabela 'tbl_usuarios' criada ou já existente.")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
finally:
    # Fechando a comunicação com o banco de dados
    if cur:
        cur.close()
    if conn:
        conn.close()
