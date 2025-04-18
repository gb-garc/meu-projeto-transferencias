import json
import requests

escolha=0
token=""

URL_base = "https://meu-projeto-transferencias-production.up.railway.app/"

while True:
    print('1 - Cadastrar usuário')
    print('2 - Fazer login')
    print('3 - Solicitar')
    print('4 - Autorizar')
    print('5 - Concluir')
    print('6 - Cancelar')
    
    escolha=int(input('Escolha:'))
    complementoURL="/"
    if escolha==1:
        username=input("Nome do username: ")
        senha=input("Senha: ")
        complementoURL="transferencias/usuarios/cadastrar"
        params={"username":username,"password":senha}
        response=requests.post(URL_base + complementoURL,headers="",params=params)
        
    elif escolha==2:
        username=input("Nome do username: ")
        password=input("password: ")
        params={"username":username,"password":password}
        complementoURL="transferencias/login"
        response=requests.post(URL_base + complementoURL,params=params)
        token=response.json()['token']

    elif escolha==3:
        id_func=input("ID funcionario: ")
        nova_obra=input("Nova obra: ")
        params = {"id_func": id_func,"nova_obra": nova_obra}
        complementoURL="transferencias/solicitar"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        response=requests.post(URL_base+complementoURL, headers=headers, params=params)

    elif escolha==4:
        id_transf=input("ID transferencia: ")
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        complementoURL=f"transferencias/autorizar/{id_transf}"
        response=requests.patch(URL_base+complementoURL, headers=headers,params="")
        
    elif escolha==5:
        id_transf=input("ID transferencia: ")
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        complementoURL=f"transferencias/concluir/{id_transf}"
        response=requests.patch(URL_base+complementoURL, headers=headers)
        
    elif escolha==6:
        id_transf=input("ID transferencia: ")
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        complementoURL=f"transferencias/cancelar/{id_transf}"
        response=requests.patch(URL_base+complementoURL, headers=headers)
        
    elif escolha==7:
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
        complementoURL="transferencias/listafuncionarios"
        response=requests.get(URL_base+complementoURL, headers=headers)
        funcionarios=response.json()["funcionarios"]

    else:
        break

    print("Status Code:", response.status_code)
    print("Resposta:", response.json())
    print('-------------------------------------------------------')

