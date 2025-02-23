from config.database import get_connection

def solicitar_transferencia(id_func, nova_obra):
    """
    Cria uma nova transferência no BD, situação 'pendente', 
    se id_func existir e obra_atual != nova_obra.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Verifica se o funcionário existe e obtém a obra atual
        cur.execute("""
            SELECT obra_atual FROM tblFuncionarios WHERE id_func = %s
        """, (id_func,))
        row = cur.fetchone()

        if not row:
            return (False, "Funcionário não encontrado.")

        obra_atual = row[0]

        if obra_atual == nova_obra:
            return (False, "Funcionário já está na obra informada.")

        # Cria a transferência com situação 'pendente'
        cur.execute("""
            INSERT INTO tbl_transferencias (id_func, nova_obra, situacao)
            VALUES (%s, %s, 'pendente')
        """, (id_func, nova_obra))

        conn.commit()
        cur.close()
        conn.close()

        return (True, "Transferência criada com sucesso.")

    except Exception as e:
        print(f"Erro ao criar transferência: {e}")
        return (False, "Erro ao criar transferência.")


def autorizar_transferencia(id_transf):
    """
    Se a transferência estiver 'pendente', altera para 'autorizada'.
    Caso contrário, retorna mensagem com a situação atual.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Verifica situação atual
        cur.execute("""
            SELECT situacao FROM tbl_transferencias WHERE id_transf = %s
        """, (id_transf,))
        row = cur.fetchone()

        if not row:
            return (False, "Transferência não encontrada.")
        
        situacao_atual = row[0]

        if situacao_atual == 'pendente':
            cur.execute("""
                UPDATE tbl_transferencias
                SET situacao = 'autorizada'
                WHERE id_transf = %s
            """, (id_transf,))
            conn.commit()
            msg = "Transferência autorizada com sucesso."
        else:
            msg = f"O processo não foi realizado. A situação atual da transferência é: {situacao_atual}"

        cur.close()
        conn.close()

        # Verifica se realmente alterou
        if situacao_atual == 'pendente':
            return (True, msg)
        else:
            return (False, msg)

    except Exception as e:
        print(f"Erro ao autorizar transferência: {e}")
        return (False, "Erro ao autorizar transferência.")


def concluir_transferencia(id_transf):
    """
    Se a transferência estiver 'autorizada', altera para 'finalizada'
    e muda a obra_atual do funcionário na tblFuncionarios.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Verifica informações da transferência
        cur.execute("""
            SELECT id_func, nova_obra, situacao
            FROM tbl_transferencias
            WHERE id_transf = %s
        """, (id_transf,))
        row = cur.fetchone()

        if not row:
            return (False, "Transferência não encontrada.")

        id_func, nova_obra, situacao_atual = row

        if situacao_atual == 'autorizada':
            # Atualiza para 'finalizada'
            cur.execute("""
                UPDATE tbl_transferencias
                SET situacao = 'finalizada'
                WHERE id_transf = %s
            """, (id_transf,))

            # Atualiza obra do funcionário
            cur.execute("""
                UPDATE tblFuncionarios
                SET obra_atual = %s
                WHERE id_func = %s
            """, (nova_obra, id_func))

            conn.commit()
            msg = "Transferência finalizada com sucesso."
        else:
            msg = f"O processo não foi realizado. A situação atual da transferência é: {situacao_atual}"

        cur.close()
        conn.close()

        # Retorno
        if situacao_atual == 'autorizada':
            return (True, msg)
        else:
            return (False, msg)

    except Exception as e:
        print(f"Erro ao concluir transferência: {e}")
        return (False, "Erro ao concluir transferência.")


def cancelar_transferencia(id_transf):
    """
    Se a transferência estiver 'pendente' ou 'autorizada', altera para 'cancelada'.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Verifica situação atual
        cur.execute("""
            SELECT situacao FROM tbl_transferencias WHERE id_transf = %s
        """, (id_transf,))
        row = cur.fetchone()

        if not row:
            return (False, "Transferência não encontrada.")
        
        situacao_atual = row[0]

        if situacao_atual in ['pendente', 'autorizada']:
            cur.execute("""
                UPDATE tbl_transferencias
                SET situacao = 'cancelada'
                WHERE id_transf = %s
            """, (id_transf,))
            conn.commit()
            msg = "Transferência cancelada com sucesso."
            ok = True
        else:
            msg = "Não foi possível completar a solicitação"
            ok = False

        cur.close()
        conn.close()

        return (ok, msg)

    except Exception as e:
        print(f"Erro ao cancelar transferência: {e}")
        return (False, "Erro ao cancelar transferência.")
