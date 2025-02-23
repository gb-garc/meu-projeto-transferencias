from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer
from models.auth_model import autenticar_usuario, verificar_token, cadastrar_usuario
from models.transfer_model import (
    solicitar_transferencia,
    autorizar_transferencia,
    concluir_transferencia,
    cancelar_transferencia
)

router = APIRouter(prefix="/transferencias", tags=["Transferências"])
security = HTTPBearer()  # Middleware de segurança para verificar tokens JWT

@router.post("/usuarios/cadastrar")
def cadastrar(username: str, senha: str):
    sucesso, mensagem = cadastrar_usuario(username, senha)
    if not sucesso:
        raise HTTPException(status_code=400, detail=mensagem)
    return {"sucesso": True, "mensagem": mensagem}

@router.post("/login")
def login(username: str, password: str):
    sucesso, resultado = autenticar_usuario(username, password)
    if not sucesso:
        raise HTTPException(status_code=401, detail=resultado)
    return {"token": resultado}

@router.post("/solicitar")
def solicitar(id_func: int, nova_obra: str, token: str = Depends(security)):
    valido, mensagem = verificar_token(token.credentials)
    if not valido:
        raise HTTPException(status_code=401, detail=mensagem)
    sucesso, mensagem = solicitar_transferencia(id_func, nova_obra)
    return {"sucesso": sucesso, "mensagem": mensagem}


@router.patch("/autorizar/{id_transf}")
def autorizar(id_transf: int, token: str = Depends(security)):
    valido, mensagem = verificar_token(token.credentials)
    if not valido:
        raise HTTPException(status_code=401, detail=mensagem)
    sucesso, mensagem = autorizar_transferencia(id_transf)
    return {"sucesso": sucesso, "mensagem": mensagem}


@router.patch("/concluir/{id_transf}")
def concluir(id_transf: int, token: str = Depends(security)):
    valido, mensagem = verificar_token(token.credentials)
    if not valido:
        raise HTTPException(status_code=401, detail=mensagem)
    sucesso, mensagem = concluir_transferencia(id_transf)
    return {"sucesso": sucesso, "mensagem": mensagem}


@router.patch("/cancelar/{id_transf}")
def cancelar(id_transf: int, token: str = Depends(security)):
    valido, mensagem = verificar_token(token.credentials)
    if not valido:
        raise HTTPException(status_code=401, detail=mensagem)
    sucesso, mensagem = cancelar_transferencia(id_transf)
    return {"sucesso": sucesso, "mensagem": mensagem}
