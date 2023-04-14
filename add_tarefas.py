import requests

def adicionar_tarefa(nome, descricao, data):
    url = 'https://api.amazon.com/add_tarefa'
    headers = {'Authorization': 'Bearer <seu-token-da-API>'}
    dados = {'nome': nome, 'descricao': descricao, 'data': data}
    resposta = requests.post(url, headers=headers, json=dados)
    if resposta.status_code == 200:
        return True
    else:
        return False