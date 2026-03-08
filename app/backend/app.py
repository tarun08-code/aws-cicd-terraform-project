from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

TASKS_FILE = 'tasks.json'

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    with open(TASKS_FILE, 'r') as f:
        tasks = json.load(f)
    return jsonify(tasks), 200

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = {
        'id': len(get_all_tasks()) + 1,
        'title': data.get('title'),
        'completed': False
    }
    tasks = get_all_tasks()
    tasks.append(task)
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)
    return jsonify(task), 201

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = get_all_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)
    return jsonify({"message": "Task deleted"}), 200

def get_all_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
