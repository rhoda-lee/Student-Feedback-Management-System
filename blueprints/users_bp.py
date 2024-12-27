import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, jsonify, request
from config.config import session
from models import *
from CRUD.user_crud import UserCrud
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash

users_bp = Blueprint('users', __name__)
user_crud = UserCrud(session)

@users_bp.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"error": "Missing required fields: username, email, or password."}), 400

        existing_user = user_crud.get_user_by_email(email)
        if existing_user:
            return jsonify({"error": "Email already exists. Please log in."}), 409

        user_crud.add_user(username, email, password)
        return jsonify({"message": "Registration successful!"}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/login', methods=['POST'])
def login_user_route():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Missing email or password."}), 400

        user = user_crud.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return jsonify({"message": f"Welcome back, {user.username}!"}), 200
        else:
            return jsonify({"error": "Invalid email or password."}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        logout_user()
        return jsonify({"message": "You have been logged out."}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    try:
        if current_user.role == RoleType.ADMIN:
            return jsonify({
                "message": "Welcome to the Admin Dashboard.",
                "AdminPanel": {
                    "username": current_user.username,
                    "email": current_user.email,
                    "admin_tools": [
                        "User Management",
                        "Feedback Reports",
                        "System Logs"
                    ]
                }
            }), 200
        
        elif current_user.role == RoleType.USER:
            return jsonify({
                "message": "Welcome to the Student Dashboard.",
                "StudentPanel": {
                    "username": current_user.username,
                    "email": current_user.email,
                    "student_tools": [
                        "Submit Feedback",
                        "View Submitted Feedback"
                    ]
                }
            }), 200
        
        else:
            return jsonify({"error": "Unauthorized role access."}), 403

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/users', methods=['GET'])
def list_users():
    try:
        users = user_crud.get_all_users()
        user_list = [{
            "id": user.user_id,
            "username": user.username,
            "email": user.email,
            "role": user.role.name
            } for user in users]
        
        return jsonify({"Users": user_list}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_crud.get_user_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found."}), 404
        return jsonify({
            "id": user.user_id,
            "username": user.username,
            "email": user.email,
            "role": user.role.name
        }), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        user = user_crud.update_user(user_id, username, email, password, role)
        if not user:
            return jsonify({"error": "User not found."}), 404

        return jsonify({"message": "User updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@users_bp.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = user_crud.delete_user(user_id)
        if user:
            return jsonify({"message": user}), 200
        return jsonify({"error": "User not found."}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
