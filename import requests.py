import json
import requests

API_URL = "https://meu-projeto-transferencias-production.up.railway.app/transferencias/solicitar"

# Parâmetros passados na URL
params = {
    "id_func": 1,
    "nova_obra": 202
}

headers = {
    "Content-Type": "application/json"
}

# Enviando a requisição POST com parâmetros na URL
#response = requests.post(API_URL, headers=headers, params=params)
response=requests.patch('https://meu-projeto-transferencias-production.up.railway.app/transferencias/cancelar/2')
#,headers=headers)
print("Status Code:", response.status_code)
print("Resposta:", response.json())


#@router.post("/solicitar")
#def solicitar(id_func: int, nova_obra: str):

#@router.patch("/autorizar/{id_transf}")
#def autorizar(id_transf: int):

#@router.patch("/concluir/{id_transf}")
#def concluir(id_transf: int):

#@router.patch("/cancelar/{id_transf}")
#def cancelar(id_transf: int):