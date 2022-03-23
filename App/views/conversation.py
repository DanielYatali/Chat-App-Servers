from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import login_required

from App.controllers import (
    create_conversation,
    save_message,
    get_all_conversations,
    get_conversation_messages
)


conversation_views = Blueprint('conversation_views', __name__, template_folder='../templates')


@conversation_views.route('/save/message', methods=['POST'])
@jwt_required()
def add_message():
    message = request.get_json();
    return jsonify(save_message(message['sender_name'], message['conversation_name'], message['content'], message['datetime']))



@conversation_views.route('/add/conversation', methods=['POST'])
@jwt_required()
def add_conversation():
    data = request.get_json();
    return jsonify(create_conversation(data['conversation_name']))

@conversation_views.route('/conversations', methods=['GET'])
def get_conversations():
    return jsonify(get_all_conversations())


@conversation_views.route('/conversation/messages', methods=['POST'])
# @jwt_required()
def get_the_conversation_messages():
    data = request.get_json()
    return jsonify(get_conversation_messages(data['conversation_name']))