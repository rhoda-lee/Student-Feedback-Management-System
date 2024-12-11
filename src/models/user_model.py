from config import session
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.role_id'), nullable=False)
    
    role = relationship('Roles', back_populates='user')
    feedbacks = relationship('Feedback', back_populates='user')

    def __str__(self):
        return f"User's ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Role ID: {self.role_id}"

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email}, role_id={self.role_id})>"


if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Tables created successfully!')
    except Exception as e:
        print(f'An error occured: {e}')