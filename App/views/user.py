from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    get_all_users,
    get_all_users_json,
    signup,
    get_user_id
)


user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/signup', methods=['POST'])
def sign_up():
    userdata = request.get_json()
    return jsonify(signup(userdata['username'],userdata['email'], userdata['password']))

@user_views.route('/user/<username>', methods=['GET'])
@jwt_required()
def user_id(username):
    return jsonify(get_user_id(username)), 200

@user_views.route('/identify')
@jwt_required()
def protected():
    return jsonify(current_identity.toDict())