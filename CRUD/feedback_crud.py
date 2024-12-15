import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),  '..')))
from config.config import session
from models import Feedback

class FeedbackCrud:
    def __init__(self, session):
        self.session = session

    def add_feedback(self, user_id, question_id, response):
        new_feedback = Feedback(user_id = user_id, question_id = question_id, response = response)
        if new_feedback:
            new_feedback.response = response
            self.session.add(new_feedback)
            self.session.commit()

            return new_feedback
        
    def get_all_feedback(self):
        return self.session.query(Feedback).all()
        
    def get_feedback_by_id(self, feedback_id):
        return self.session.query(Feedback).filter_by(feedback_id = feedback_id).first()
    
    def get_feedback_by_user(self, user_id):
        return self.session.query(Feedback).filter_by(user_id = user_id).first()
    
    def get_feedback_by_question(self, question_id):
        return self.session.query(Feedback).filter_by(question_id = question_id).first()
    
    def update_feedback(self, feedback_id, response):
        feedback = self.session.query(Feedback).filter_by(feedback_id = feedback_id).first()

        if feedback:
            feedback.response = response
            self.session.commit()
            return feedback
        return None
    
    def delete_feedback(self, feedback_id):
        feedback = self.session.query(Feedback).filter_by(feedback_id = feedback_id).first()

        if feedback:
            self.session.delete(feedback)
            return f'Feedback with feedback id: {feedback_id} has been removed.'
        return False