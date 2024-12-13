import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  '..')))
from config.config import session
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text
from enum import Enum as PyEnum

Base = declarative_base()


class RoleType(PyEnum):
    USER = 'user',
    ADMIN = 'admin'


class User(Base): 
    __tablename__ = 'users' 
    user_id = Column(Integer, primary_key = True) 
    username = Column(String(50), unique = True, nullable = False) 
    email = Column(String(100), unique = True, nullable = False) 
    password = Column(String(200), nullable = False) 
    role = Column(Enum(RoleType), default = RoleType.USER, nullable = False)

    feedback = relationship("Feedback", back_populates = "users")
    

    def __str__(self):
        return f"User's ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Role ID: {self.role_id}"

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email}, role_id={self.role_id})>"




'''Questions Table'''

class QuestionTypeEnum(PyEnum):
    TEXT = "text"
    SELECT = "select"

class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String(255), nullable=False)
    question_type = Column(Enum(QuestionTypeEnum), nullable=False)
    options = Column(String(500))




'''Feedback Table'''
class Feedback(Base):
    __tablename__ = "feedback"
    feedback_id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable = False)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable = False)
    response = Column(Text(500), nullable = False)

    users = relationship("User", back_populates = "feedback")
    question = relationship("Question", back_populates = "feedback")


    def __str__(self):
        return f"Feedback ID: {self.feedback_id}, User ID: {self.user_id}, Question ID: {self.question_id}, Response: {self.response}"


    def __repr__(self):
        return f"<Feedback(feedback_id={self.feedback_id}, user_id={self.user_id}, question_id={self.question_id}, response={self.response})>"
    
if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Tables created successfully!')
    except Exception as e:
        print(f'An error occured: {e}')

