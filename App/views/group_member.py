from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import login_required

from App.controllers import (
    get_all_group_members,
    add_member,
    remove_member,
    get_all_member_messages
)

group_member_views = Blueprint('group_member_views', __name__, template_folder='../templates')


@group_member_views.route('/<conversation_name>/members', methods=['GET'])
@jwt_required()
def list_group_members(conversation_name):
    return jsonify(get_all_group_members(conversation_name))



@group_member_views.route('/conversation/join', methods=['POST'])
@jwt_required()
def add_group_member():
    data = request.get_json();
    return add_member(data['conversation_name'], data['username'], data['datetime'])

@group_member_views.route('/conversation/remove_member', methods=['DELETE'])
def remove_conversation_member():
    data = request.get_json()
    return jsonify(remove_member(data['conversation_name'],data['username']))


# @group_member_views.route('/conversation/member/messages', methods=['POST'])
# @jwt_required()
# def get_the_conversation_messages():
#     data = request.get_json()
#     return jsonify(get_all_member_messages(data['conversation_name'], data['username']))