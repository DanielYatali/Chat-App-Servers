
from App.models import Conversation, Message, User, message
from App.database import db


def save_message(sender_name, conversation_id, content, datetime):
    conversation = Conversation.query.get(conversation_id)
    if not conversation:
        return {
            "message": "conversation does not exist"
        }
    new_message = Message(sender_name=sender_name, conversation_id=conversation_id, content = content, datetime=datetime)
    db.session.add(new_message)
    conversation.messages.append(new_message)
    db.session.commit()
    return {
        "message": "message added"
    }

def create_conversation(conversation_name, private):
    conversation = Conversation.query.filter_by(conversation_name = conversation_name).first()
    if conversation:
        return {
            "message": "conversation already exists"
            }

    new_conversation = Conversation(conversation_name=conversation_name, private =private)
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

def get_conversation_messages(conversation_id):
    conversation = Conversation.query.get(conversation_id)
    if not conversation:
        return {
            "message": "conversation does not exist"
        }
    # messages = Message.query.filter_by(conversation_name = conversation_name)
    if not conversation.messages:
        return []
    
    messages = [message.toDict() for message in conversation.messages]
    return messages

def get_user_conversations(user_id):
    user = User.query.get(user_id)
    if not user:
        return{
            "message": "user does not exist"
        }
    conversations = [conversation.toDict() for conversation in user.conversations]
    return conversations

def get_conversation_users(conversation_id):
    conversation = Conversation.query.get(conversation_id)
    if not conversation:
        return{
            "message": "conversation does not exist"
        }
    users = [user.toDict() for user in conversation.users]
    return users


def join_conversation(user_id, conversation_id):
    join_conversation = Conversation.query.get(conversation_id)
    
    if not join_conversation:
        return{
            'message': "conversation does not exist"
        }
    user = User.query.get(user_id)
    if not user:
        return{
            'message': "user does not exist"
        }
    for conversation in user.conversations:
        if conversation.id == conversation_id:
            return{
                "message": "you have already joined this group"
            }

    if(len(join_conversation.users) == 2 and join_conversation.private):
        return{
            "message": "conversation is private and already contains 2 users"
        }
    user.conversations.append(join_conversation)
    db.session.add(user)
    db.session.commit()
    return {
        'message': f"user joined {join_conversation.conversation_name}"
    }