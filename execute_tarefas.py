import requests

url = "http://192.168.0.100:5000/tasks"
headers = {'Content-type': 'application/json'}

# GET /tasks
response = requests.get(url)
tasks = response.json()
print(tasks)

# POST /tasks
new_task = {"description": "Fazer compras no mercado", "status": "em andamento"}
response = requests.post(url, json=new_task, headers=headers)
if response.status_code == 201:
    print("Tarefa criada com sucesso!")
