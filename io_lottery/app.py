from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'error': 'Not Implemented'}), 501

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.json
    for i, user in enumerate(users):
        if user['id'] == user_id:
            users[i] = updated_user
            return jsonify(updated_user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    user_data = request.json
    for i, user in enumerate(users):
        if user['id'] == user_id:
            user.update(user_data)
            return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            del users[i]
            return '', 204
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
