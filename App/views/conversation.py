from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity
from flask_login import login_required
import jwt

from App.controllers import (
    create_conversation,
    save_message,
    get_all_conversations,
    get_conversation_messages,
    get_user_conversations,
    get_conversation_users,
    join_conversation,
    check_conversation_talk,
    get_user_conversations_and_info
)
from App.controllers.conversation import check_conversation_talk, create_matches_coversations, get_user_conversations_and_info


conversation_views = Blueprint('conversation_views', __name__, template_folder='../templates')


@conversation_views.route('/save/message', methods=['POST'])
@jwt_required()
def add_message():
    message = request.get_json();
    return jsonify(save_message(current_identity, message['conversation_id'], message['content'], message['datetime']))

@conversation_views.route('/add/conversation', methods=['POST'])
@jwt_required()
def add_conversation():
    data = request.get_json();
    return jsonify(create_conversation(data['conversation_name'], data['private']))

@conversation_views.route('/conversations', methods=['GET'])
def get_conversations():
    return jsonify(get_all_conversations())


@conversation_views.route('/<conversation_id>/messages', methods=['GET'])
@jwt_required()
def get_the_conversation_messages(conversation_id):
    return jsonify(get_conversation_messages(conversation_id))

@conversation_views.route('/<user_id>/conversations', methods=['GET'])
@jwt_required()
def get_all_user_conversations(user_id):
    return jsonify(get_user_conversations(user_id))

@conversation_views.route('/<conversation_id>/users', methods=['GET'])
@jwt_required()
def get_all_users_conversation(conversation_id):
    return jsonify(get_conversation_users(conversation_id))

@conversation_views.route('/conversation/join', methods=['POST'])
@jwt_required()
def add_user_to_conversation():
    data = request.get_json()
    return jsonify(join_conversation(data['user_id'], data['conversation_id']))

@conversation_views.route('/conversation/<sender_id>/<receiver_id>', methods=['GET'])
@jwt_required()
def check_conversation(sender_id, receiver_id):
    return jsonify(check_conversation_talk(sender_id, receiver_id))

@conversation_views.route('/conversation/create/matches', methods=['POST'])
@jwt_required()
def create_conversation_matches():
    matches = request.get_json()
    return jsonify(create_matches_coversations(current_identity, matches))

@conversation_views.route('/user/conversations/user_info', methods=['GET'])
@jwt_required()
def get_all_user_conversations_and_user_information():
    return jsonify(get_user_conversations_and_info(current_identity))