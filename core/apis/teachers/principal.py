
from flask import Blueprint, request, jsonify
from models import Teacher
from config import db

teachers_bp = Blueprint('teachers', __name__)

@teachers_bp.route('/principal/teachers', methods=['GET'])
def get_all_teachers():
    if 'X-Principal' not in request.headers:
        return jsonify({"error": "Unauthorized"}), 403

    principal_id = request.headers.get('X-Principal')
    teachers = Teacher.query.all()
    result = [teacher.to_dict() for teacher in teachers]
    return jsonify({"data": result})
