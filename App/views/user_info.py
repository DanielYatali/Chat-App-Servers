from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_user_info,
    get_user_info,
    update_user_info,
    match,
    create_update_user_info
)


user_info_views = Blueprint('user_info_views', __name__, template_folder='../templates')


@user_info_views.route('/user/create_info', methods=['POST'])
@jwt_required()
def add_user_info():
    data = request.get_json()
    return jsonify(create_user_info(data)), 201

@user_info_views.route('/<user_id>/info', methods=['GET'])
@jwt_required()
def get_info_for_user(user_id):
    return jsonify(get_user_info(user_id))

@user_info_views.route('/user/info', methods=['GET'])
@jwt_required()
def get_info_for_current_user():
    return jsonify(get_user_info(current_identity.id))

@user_info_views.route('/user/update_info', methods=['POST'])
@jwt_required()
def update_info_for_user():
    data = request.get_json()
    return jsonify(update_user_info(data)), 200

#if user info exist update it with info if it does not then create it
@user_info_views.route('/user/create/update_info', methods=['POST'])
@jwt_required()
def update_create_info_for_user():
    data = request.get_json()
    return jsonify(create_update_user_info(current_identity, data)), 200

@user_info_views.route('/<user_id>/match', methods = ['GET'])
@jwt_required()
def get_matches(user_id):
    return jsonify(match(user_id)), 200