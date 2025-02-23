import os
import jwt
import datetime
from passlib.context import CryptContext
from config.database import get_connection

# Chave secreta para assinar os tokens
SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-muito-segura")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(SECRET_KEY)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Configuração do bcrypt para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para gerar hash da senha
def hash_senha(senha):
    return pwd_context.hash(senha)

# Função para verificar a senha digitada com o hash armazenado
def verificar_senha(senha_digitada, senha_hash):
    return pwd_context.verify(senha_digitada, senha_hash)

# Função para gerar token JWT
def gerar_token(username):
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # Expira em 2h
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Função para autenticar usuário e gerar token
def autenticar_usuario(username, senha):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT password_hash FROM tbl_usuarios WHERE username = %s", (username,))
        row = cur.fetchone()

        cur.close()
        conn.close()

        if row and verificar_senha(senha, row[0]):
            return True, gerar_token(username)
        
        return False, "Credenciais inválidas."

    except Exception as e:
        return False, f"Erro ao autenticar: {str(e)}"

# Função para verificar token JWT
def verificar_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True, payload["sub"]
    except jwt.ExpiredSignatureError:
        return False, "Token expirado"
    except jwt.InvalidTokenError:
        return False, "Token inválido"
