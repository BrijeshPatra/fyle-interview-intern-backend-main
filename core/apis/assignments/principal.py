from flask import Blueprint, request, jsonify
from models import assignments

assignments_bp=Blueprint('assignments',__name__)

@assignments.bp.route('/principal/assignments' ,methods=['GET'])

def get_all_assignments():
    if 'X-Principal' not in request.headers:
        return jsonify({"error":"Unauthorized"}),403
    
    principal_id=request.headers.get('X-Principal') 
    assignments=assignments.query.all()
    result=[assignments.to_dict() for assignment in assignments]
    return jsonify({"data":result})