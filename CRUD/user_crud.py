import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  '..')))
from config.config import session
from models import User, RoleType
from werkzeug.security import generate_password_hash, check_password_hash

class UserCrud:
    def __init__(self, session):
        self.session = session

    def add_user(self, username, email, password, role = RoleType.USER):
        hashed_password = generate_password_hash(password, method = 'pbkdf2:sha256')
        new_user = User(username = username, email = email, password = hashed_password, role = role)
        self.session.add(new_user)
        self.session.commit()
        return new_user
    
    # def verify_password(self, password):
    #     return check_password_hash(self.password, password)
    
    def authenticate_user(self, email, password):
        user = self.session.query(User).filter_by(email=email).first()
        
        if not user:
            return {"error": "User not found"}, 404
        
        if check_password_hash(user.password, password):
            return {"message": "Login successful", "user_id": user.id}, 200
        return {"error": "Incorrect password"}, 401

    
    def get_all_users(self):
        return self.session.query(User).all()

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter_by(user_id = user_id).first()
    
    def get_user_by_email(self, email):
        return self.session.query(User).filter_by(email = email).first()
    
    def update_user(self, user_id, username = None, email = None, password = None, role = None):
        user = self.session.query(User).filter_by(user_id = user_id).first()

        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = generate_password_hash(password, method = 'pbkdf2:sha256')
            if role:
                user.role = role
            self.session.commit()
        return user
    
    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(user_id = user_id).first()

        if user:
            self.session.delete(user)
        self.session.commit()
        return f'User with ID: {user_id} has been deleted!'
    



    