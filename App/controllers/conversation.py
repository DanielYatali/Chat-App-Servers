from App.models import Conversation, Message
from App.database import db


def save_message(sender_name, conversation_name, content, datetime):
    conversation = Conversation.query.filter_by(conversation_name = conversation_name).first()
    if not conversation:
        return {
            "message": "conversation does not exist"
        }
    new_message = Message(sender_name=sender_name, conversation_name=conversation_name, content = content, datetime=datetime)
    db.session.add(new_message)
    db.session.commit()
    return {
        "message": "message added"
    }

def create_conversation(conversation_name):
    conversation = Conversation.query.filter_by(conversation_name = conversation_name).first()
    if conversation:
        return {
            "message": "conversation already exists"
            }

    new_conversation = Conversation(conversation_name=conversation_name)
    db.session.add(new_conversation)
    db.session.commit()
    return {
        "message": "conversation created"
    }
    

def get_all_conversations():
    conversations = Conversation.query.all()
    if not conversations:
        return []
    
    conversations = [conversation.toDict() for conversation in conversations]
    return conversations

def get_conversation_messages(conversation_name):
    conversation = Conversation.query.filter_by(conversation_name=conversation_name).first()
    if not conversation:
        return {
            "message": "conversation does not exist"
        }
    messages = Message.query.filter_by(conversation_name = conversation_name)
    if not messages:
        return []
    
    messages = [message.toDict() for message in messages]
    return messages
    