import sqlite3
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    nome = request.json['nome']
    descricao = request.json['descricao']
    data = request.json['data']

    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tarefas (nome, descricao, data) VALUES (?, ?, ?)', (nome, descricao, data))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Tarefa adicionada com sucesso!'})

@app.route('/editar_tarefa', methods=['PUT'])
def editar_tarefa():
    id = request.json['id']
    nome = request.json['nome']
    descricao = request.json['descricao']
    data = request.json['data']

    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET nome=?, descricao=?, data=? WHERE id=?', (nome, descricao, data, id))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Tarefa editada com sucesso!'})

@app.route('/excluir_tarefa', methods=['DELETE'])
def excluir_tarefa():
    id = request.json['id']

    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id=?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': 'Tarefa excluída com sucesso!'})

@app.route('/listar_tarefas', methods=['GET'])
def listar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = []
    for linha in cursor.fetchall():
        tarefa = {'id': linha[0], 'nome': linha[1], 'descricao': linha[2], 'data': linha[3]}
        tarefas.append(tarefa)
    conn.close()

    return jsonify(tarefas)