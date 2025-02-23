from fastapi import APIRouter
from models.transfer_model import (
    solicitar_transferencia,
    autorizar_transferencia,
    concluir_transferencia,
    cancelar_transferencia
)

router = APIRouter(prefix="/transferencias", tags=["Transferências"])


@router.post("/solicitar")
def solicitar(id_func: int, nova_obra: str):
    sucesso, mensagem = solicitar_transferencia(id_func, nova_obra)
    return {"sucesso": sucesso, "mensagem": mensagem}


@router.patch("/autorizar/{id_transf}")
def autorizar(id_transf: int):
    sucesso, mensagem = autorizar_transferencia(id_transf)
    return {"sucesso": sucesso, "mensagem": mensagem}


@router.patch("/concluir/{id_transf}")
def concluir(id_transf: int):
    sucesso, mensagem = concluir_transferencia(id_transf)
    return {"sucesso": sucesso, "mensagem": mensagem}


@router.patch("/cancelar/{id_transf}")
def cancelar(id_transf: int):
    sucesso, mensagem = cancelar_transferencia(id_transf)
    return {"sucesso": sucesso, "mensagem": mensagem}
