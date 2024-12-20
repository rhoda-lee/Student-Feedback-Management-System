import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  '..')))
from config.config import session
from models import Question, QuestionTypeEnum
import json

class QuestionCrud:
    def __init__(self, session):
        self.session = session

    def add_question(self, question_text, question_type = QuestionTypeEnum.TEXT, options = None):
        options_json = json.dumps(options) if options else None
        question = Question(
            question_text = question_text,
            question_type = question_type,
            options = options_json
        )
        try:
            self.session.add(question)
            self.session.commit()
            return question
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error adding question: {e}")
        
    
    def get_all_questions(self):
        try:
            return self.session.query(Question).all()
        except Exception as e:
            raise Exception(f"Error retrieving all questions: {e}")
    
    
    def get_question_by_id(self, question_id):
        try:
            return self.session.query(Question).filter_by(question_id=question_id).first()
        except Exception as e:
            raise Exception(f"Error retrieving question by ID: {e}")
    
    
    def update_question(self, question_id, question_text = None, question_type = None, options = None):
        question = self.session.query(Question).filter_by(question_id = question_id).first()

        if not question:
            raise Exception("Question not found")

        try:
            if question:
                if question_text:
                    question.question_text = question_text
                if question_type:
                    question.question_type = question_type
                if options is not None:
                    question.options = json.dumps(options) if options else json.dumps([])
            
            self.session.commit()
            return question
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error updating question: {e}")
    
    def delete_question(self, question_id):
        question = self.session.query(Question).filter_by(question_id = question_id).first()

        if not question:
            return None

        try:
            self.session.delete(question)
            self.session.commit()
            return question
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error deleting question: {e}")
        
    def delete_all_questions(self):
        try:
            self.session.query(Question).delete()
            self.session.commit()
            return f'All questions have been deleted!'
        except Exception as e:
            self.session.rollback()
            return f'Error while deleting all questions: {e}'


