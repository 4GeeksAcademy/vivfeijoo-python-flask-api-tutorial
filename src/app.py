from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista global de tareas
todos = [
    { "label": "My first task", "done": False }
]

# GET /todos - Obtener la lista de tareas
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST /todos - Agregar una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    todos.append(request_body)
    return jsonify(todos)

# DELETE /todos/<int:position> - Eliminar una tarea por su índice
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    if 0 <= position < len(todos):
        todos.pop(position)

    return jsonify(todos)

# Ejecutar servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)



