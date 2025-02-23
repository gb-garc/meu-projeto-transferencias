import json
import requests


# Parâmetros passados na URL
params = {
    "id_func": 1,
    "nova_obra": 202
}

headers = {"Content-Type": "application/json"}

escolha=0
print('1 - Cadastrar usuário')
print('2 - Fazer login')
print('3 - Solicitar')
print('4 - Autorizar')
print('5 - Concluir')
print('6 - Cancelar')

escolha=int(input('Escolha:'))

API_URL = 'https://meu-projeto-transferencias-production.up.railway.app{}'.format("A")
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