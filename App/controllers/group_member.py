from App.models import Conversation, Group_member, Message
from App.database import db


def is_member(conversation_name, username):
    member = Group_member.query.filter_by(conversation_name=conversation_name, username=username).first()
    if member:
        return True
    return False


def get_all_group_members(conversation_name):
    conversation = Conversation.query.filter_by(conversation_name= conversation_name).first()
    if not conversation:
        return{
            "message":"conversation does not exist"

        }

    members = Group_member.query.filter_by(conversation_name=conversation_name)
    if not members:
        return{
            "message":"empty"
        }
    
    members = [member.toDict() for member in members]
    return members

def add_member(conversation_name, username, joined_datetime):
    conversation = Conversation.query.filter_by(conversation_name=conversation_name).first()
    if not conversation:
        return{
            "message": "conversation does not exist"
        }
    if is_member(conversation_name,username):
        return{
            "message": "you have already joined group"
        }
    group_member = Group_member(username=username, conversation_name=conversation_name, joined_datetime=joined_datetime)
    db.session.add(group_member)
    db.session.commit()
    return{
        "message": "join successful"
    }
    

def remove_member(conversation_name, username):
    conversation = Conversation.query.filter_by(conversation_name=conversation_name).first()
    if not conversation:
        return{
            "message": "conversation does not exist"
        }
    member = Group_member.query.filter_by(username=username, conversation_name=conversation_name).first()
    if not member:
        return{
            "message": "you have not joined this group"
        }
    db.session.delete(member)
    res = db.session.commit()
    return res


def get_all_member_messages(conversation_name, username):
    messages = Message.query.filter_by(sender_name=username, conversation_name=conversation_name)
    if not messages:
        return []
    return messages


















