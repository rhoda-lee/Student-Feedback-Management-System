from flask import Blueprint, jsonify, request
from flask_login import login_required
from models import Question, QuestionTypeEnum
from config.config import session
from CRUD.question_crud import QuestionCrud
import json

questions_bp = Blueprint('questions', __name__)
question_crud = QuestionCrud(session)

@questions_bp.route('/questions', methods=['POST'])
@login_required
def add_question():
    try:
        data = request.get_json()
        question_text = data.get('question_text')
        question_type = data.get('question_type')
        options = data.get('options')

        if not question_text or not question_type:
            return jsonify({"Error": "Missing required fields: question_text or question_type."}), 400

        if question_type == QuestionTypeEnum.SELECT.value:

            if not options or not isinstance(options, list):
                return jsonify({"Error": "Options must be provided as a list for SELECT type questions."}), 400
            options = json.dumps(options)

        else:
            options = None

        question = question_crud.add_question(
            question_text,
            question_type,
            options
            )

        return jsonify({"Message": "Question created successfully!", "Question": {
            "question_id": question.question_id,
            "question_text": question.question_text,
            "question_type": question.question_type.value,
            "options": json.loads(question.options) if question.options else None
        }}), 201
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@questions_bp.route('/questions', methods=['GET'])
def list_questions():
    try:
        questions = question_crud.get_all_questions()
        question_list = [
            {
                "question_id": q.question_id,
                "question_text": q.question_text,
                "question_type": q.question_type.value,
                "options": json.loads(q.options) if q.options else None
            } for q in questions
        ]
        return jsonify({"Questions": question_list}), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@questions_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    try:
        question = question_crud.get_question_by_id(question_id)
        if not question:
            return jsonify({"Error": "Question not found."}), 404
        return jsonify({
            "question_id": question.question_id,
            "question_text": question.question_text,
            "question_type": question.question_type.value,
            "options": json.loads(question.options) if question.options else None
        }), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@questions_bp.route('/questions/update/<int:question_id>', methods=['PUT'])
@login_required
def update_question(question_id):
    try:
        data = request.get_json()
        question_text = data.get('question_text')
        question_type = data.get('question_type')
        options = data.get('options')

        if not question_text or not question_type:
            return jsonify({"Error": "Missing required fields: question_text or question_type."}), 400

        if question_type == QuestionTypeEnum.SELECT.value:
            if not options or not isinstance(options, list):
                return jsonify({"Error": "Options must be provided as a list for SELECT type questions."}), 400
            options = json.dumps(options)
        else:
            options = None

        question = question_crud.update_question(question_id, question_text, question_type, options)
        if not question:
            return jsonify({"Error": "Question not found or unauthorized to update."}), 404

        return jsonify({"Message": "Question updated successfully."}), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500

@questions_bp.route('/questions/delete/<int:question_id>', methods=['DELETE'])
@login_required
def delete_question(question_id):
    try:
        success = question_crud.delete_question(question_id)
        if not success:
            return jsonify({"Error": "Question not found or unauthorized to delete."}), 404

        return jsonify({"Message": "Question deleted successfully."}), 200
    except Exception as e:
        return jsonify({"Error": f"An error occurred: {e}"}), 500
