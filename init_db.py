import os
import psycopg2
from psycopg2 import sql

# Obtendo a URL de conexão do banco de dados a partir das variáveis de ambiente
DATABASE_URL = os.getenv('DATABASE_URL')

# Conectando ao banco de dados
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Definindo o comando SQL para criar a tabela tbl_usuarios
create_table_query = '''
CREATE TABLE IF NOT EXISTS tbl_usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
'''

# Executando o comando SQL
cur.execute(create_table_query)

# Confirmando as alterações no banco de dados
conn.commit()

# Fechando a comunicação com o banco de dados
cur.close()
conn.close()

print("Tabela 'tbl_usuarios' criada ou já existente.")
