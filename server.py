from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        return jsonify(tasks)
    elif request.method == 'POST':
        new_task = request.get_json()
        tasks.append(new_task)
        return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
