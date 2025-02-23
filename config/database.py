import os
import psycopg2

# Obtém a URL do banco de dados do Railway
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("Erro: A variável DATABASE_URL não está definida!")

def get_connection():
    #Retorna uma conexão com o banco de dados PostgreSQL no Railway.
    conn = psycopg2.connect(DATABASE_URL)
    return conn
