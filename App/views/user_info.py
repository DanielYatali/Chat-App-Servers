from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
    create_user_info,
    get_user_info,
    update_user_info,
    match
)


user_info_views = Blueprint('user_info_views', __name__, template_folder='../templates')


@user_info_views.route('/user/create_info', methods=['POST'])
@jwt_required()
def add_user_info():
    data = request.get_json()
    return jsonify(create_user_info(data['user_id'], data['user_info']))

@user_info_views.route('/user/info', methods=['GET'])
@jwt_required()
def get_info_for_user():
    data = request.get_json()
    return jsonify(get_user_info(data['user_id']))

@user_info_views.route('/user/update_info', methods=['POST'])
@jwt_required()
def update_info_for_user():
    data = request.get_json()
    return jsonify(update_user_info(data['user_id'], data['user_info']))

@user_info_views.route('/user/match', methods = ['GET'])
@jwt_required()
def get_matches():
    data = request.get_json()
    return jsonify(match(data['user_id']))