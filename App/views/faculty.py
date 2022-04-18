from flask import Blueprint,jsonify, request
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_faculty,
    add_new_major,
    get_faculty_majors,
    get_all_majors,
    get_all_faculties,
    get_faculty_by_name_majors
)


faculty_views = Blueprint('faculty_views', __name__, template_folder='../templates')



@faculty_views.route('/create/faculty', methods=['POST'])
def add_new_faculty():
    data = request.get_json()
    return jsonify(create_faculty(data['faculty_name'])), 201

@faculty_views.route('/create/major', methods=['POST'])
def create_major():
    data = request.get_json()
    return jsonify(add_new_major(data['faculty_id'], data["major_name"])), 201

@faculty_views.route('/get/majors/', methods=['GET'])
def all_majors():
    return jsonify(get_all_majors()), 201

@faculty_views.route("/get/faculties", methods=['GET'])
def all_faculty():
    return jsonify(get_all_faculties()), 201


@faculty_views.route('/get/<id>/majors', methods=['GET'])
def get_all_majors_faculty(id):
    return jsonify(get_faculty_majors(id)), 200

@faculty_views.route('/get/by_name/<name>/majors', methods=['GET'])
def get_all_majors_faculty_name(name):
    return jsonify(get_faculty_by_name_majors(name)), 200