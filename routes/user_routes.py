from doctest import debug
from flask import Blueprint, request, jsonify
from models.user_model import User

user_routes = Blueprint('user_routes', __name__)

user_model = User()

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = user_model.get_all_users()

    return jsonify([user.to_json() for user in users])

@user_routes.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = user_model.get_user(user_id=id)
    return jsonify(user)

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_model.create_user(data)
    return jsonify(user["id"])

@user_routes.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = user_model.update_user(user_id=id, user_data=data)
    return jsonify(user['id'])

@user_routes.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = user_model.delete_user(user_id=id)
    return jsonify({'message': 'User deleted'})
