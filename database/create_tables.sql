-- Criar tabela de usuários
CREATE TABLE IF NOT EXISTS tbl_usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

-- Criar tabela de Funcionários
CREATE TABLE IF NOT EXISTS tblFuncionarios (
    id_func SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    obra_atual VARCHAR(100)
);

-- Criar tabela de Transferências
CREATE TABLE IF NOT EXISTS tbl_transferencias (
    id_transf SERIAL PRIMARY KEY,
    id_func INT NOT NULL,
    nova_obra VARCHAR(100),
    situacao VARCHAR(20),
    FOREIGN KEY (id_func) REFERENCES tblFuncionarios (id_func)
);

-- Criar tabela de Permissões de Usuários
CREATE TABLE IF NOT EXISTS tbl_permissoes_usuarios (
    id_perm SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    tipo_autorizacao VARCHAR(50),
    obra VARCHAR(100)
);
