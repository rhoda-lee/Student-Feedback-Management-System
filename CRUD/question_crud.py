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
        self.session.add(question)
        self.session.commit()
        return question
    
    def get_all_questions(self):
        return self.session.query(Question).all()
    
    def get_question_by_id(self, question_id):
        return self.session.query(Question).filter_by(question_id = question_id).first()
    
    def get_question_by_id(self, question_id):
        return self.session.query(Question).filter_by(question_id = question_id).first()
    
    def update_question(self, question_id, question_text = None, question_type = None, options = None):
        question = self.session.query(Question).filter_by(question_id = question_id).first()

        if question:
            if question_text:
                question.question_text = question_text
            if question_type:
                question.question_type = question_type
            if options:
                question.options = json.dumps(options)
            self.session.commit()
        return question
    
    def delete_question(self, question_id):
        question = self.session.query(Question).filter_by(question_id = question_id).first()

        if question:
            self.session.delete(question)
            self.session.commit()
            return f'Question has been deleted!'
        
    def delete_all_questions(self):
        try:
            self.session.query(Question).delete()
            self.session.commit()
            return f'All questions have been deleted!'
        except Exception as e:
            self.session.rollback()
            return f'Error while deleting all questions: {e}'


