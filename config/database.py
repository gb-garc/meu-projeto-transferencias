import os
import psycopg2
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env (localmente)
load_dotenv()

PGHOST = os.getenv('PGHOST')
PGPORT = os.getenv('PGPORT')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
PGDATABASE = os.getenv('PGDATABASE')

def get_connection():
    """
    Retorna uma conexão com o banco de dados PostgreSQL.
    """
    conn = psycopg2.connect(
        host=PGHOST,
        port=PGPORT,
        user=PGUSER,
        password=PGPASSWORD,
        dbname=PGDATABASE
    )
    return conn
