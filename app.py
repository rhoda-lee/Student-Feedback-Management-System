from flask import Flask
from flask_login import LoginManager
from models import User
from blueprints import feedback_bp
from blueprints import users_bp
from blueprints import questions_bp
from config.config import session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login_user_route'

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

# Register blueprints
app.register_blueprint(users_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(feedback_bp)

@app.route('/')
def home():
    return {"Message": "Welcome to the Student Feedback Management System"}

if __name__ == '__main__':
    app.run(debug=True)
