from flask import Blueprint, jsonify, request
from flask_login import login_required
from models import Feedback
from config.config import session
from CRUD.feedback_crud import FeedbackCrud

feedback_bp = Blueprint('feedbacks', __name__)
feedback_crud = FeedbackCrud(session)

@feedback_bp.route('/feedback', methods=['POST'])
@login_required
def create_feedback():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        question_id = data.get('question_id')
        response = data.get('response')

        if not user_id or not question_id or not response:
            return jsonify({"Error": "Missing required fields: user_id, question_id, or response."}), 400

        feedback = feedback_crud.add_feedback(user_id, question_id, response)
        return jsonify({"Message": "Feedback created successfully!", "Feedback": {
            "feedback_id": feedback.feedback_id,
            "user_id": feedback.user_id,
            "question_id": feedback.question_id,
            "response": feedback.response
        }}), 201
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@feedback_bp.route('/feedback', methods=['GET'])
def list_feedback():
    try:
        feedbacks = feedback_crud.get_all_feedback()
        feedback_list = [
            {
                "feedback_id": f.feedback_id,
                "user_id": f.user_id,
                "question_id": f.question_id,
                "response": f.response
            } for f in feedbacks
        ]
        return jsonify({"Feedbacks": feedback_list}), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@feedback_bp.route('/feedback/<int:feedback_id>', methods=['GET'])
def get_feedback(feedback_id):
    try:
        feedback = feedback_crud.get_feedback_by_id(feedback_id)
        if not feedback:
            return jsonify({"Error": "Feedback not found."}), 404
        return jsonify({
            "feedback_id": feedback.feedback_id,
            "user_id": feedback.user_id,
            "question_id": feedback.question_id,
            "response": feedback.response
        }), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@feedback_bp.route('/feedback/update/<int:feedback_id>', methods=['PUT'])
@login_required
def update_feedback(feedback_id):
    try:
        data = request.get_json()
        response = data.get('response')

        if not response:
            return jsonify({"Error": "Missing required field: response."}), 400

        feedback = feedback_crud.update_feedback(feedback_id, response)
        if not feedback:
            return jsonify({"Error": "Feedback not found or unauthorized to update."}), 404

        return jsonify({"Message": "Feedback updated successfully."}), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@feedback_bp.route('/feedback/delete/<int:feedback_id>', methods=['DELETE'])
@login_required
def delete_feedback(feedback_id):
    try:
        success = feedback_crud.delete_feedback(feedback_id)
        if not success:
            return jsonify({"Error": "Feedback not found or unauthorized to delete."}), 404

        return jsonify({"Message": "Feedback deleted successfully."}), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500
