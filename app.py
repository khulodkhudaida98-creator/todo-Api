from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    todos.append(data)
    return jsonify({"message": "Added successfully"}), 201

@app.route('/')
def home():
    return jsonify({"message": "Todo API is running!"})

if __name__ == '__main__':
    app.run(debug=True)