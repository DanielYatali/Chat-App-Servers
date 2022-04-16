
from App.models import Conversation, Message, User, conversation
from App.database import db


def save_message(user, conversation_id, content, datetime, photo):
    conversation = Conversation.query.get(conversation_id)
    if not conversation:
        return {
            "message": "conversation does not exist"
        }
    # in_conversation = User.query.filter(User.conversations.any(id==conversation_id)).one()
    #figure out later
    user_conversations = user.conversations
    for i in user_conversations:
        if i.id == conversation_id:
            new_message = Message(sender_name=user.username, conversation_id=conversation_id, content = content, datetime=datetime, photo=photo)
            db.session.add(new_message)
            conversation.messages.append(new_message)
            db.session.commit()
            return {
                "message": "message added"
            }
    return {
        "message": "you have not joined this chat"
    }

#This function checks if two users have a chat together if they don't then a new private group will be created for them to chat
def check_conversation_talk(sender, receiver_id):
    receiver = User.query.get(receiver_id)
    if not sender or not receiver:
        return {"message": "one user does not exist"}
    convo_name1 = sender.username + '+' + receiver.username
    convo_name2 = receiver.username +'+' + sender.username
    conversation = Conversation.query.filter((Conversation.conversation_name == convo_name1) | (Conversation.conversation_name == convo_name2)).first()
    if not conversation:
        new_conversation = Conversation(conversation_name=convo_name1, private= True, photo = "none", criteria="none")
        db.session.add(new_conversation)
        db.session.commit()

        #add both users to conversation
        join_conversation(sender.id, new_conversation.id)
        join_conversation(receiver_id, new_conversation.id)
        return new_conversation.toDict()
    return conversation.toDict()


def create_conversation(conversation_name, private, photo, criteria):
    conversation = Conversation.query.filter_by(conversation_name = conversation_name).first()
    if conversation:
        return {
            "message": "conversation already exists"
            }

    new_conversation = Conversation(conversation_name=conversation_name, private=private, photo= photo, criteria= criteria)
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


def create_matches_coversations(user, person_matches):
    for match in person_matches: 
        check_conversation_talk(user, match)
    # for group_match in group_matches:
    #     join_conversation(user.id, group_match.id)
    return {"message": "conversations created"}


#Get all user's current conversations to be displayed on the side bar.
#Since some conversations may be private and some conversations may be groups some extra work needs to be done
def get_user_conversations_and_info(current_user):
    conversations = current_user.conversations #get all user conversations
    chats = []
    for conversation in conversations:
        users = conversation.users #get all users for that conversation
        if conversation.private: #only 2 users would be in the conversation if private
            for user in users:
                if(current_user.id != user.id): #find the other user
                    other_user = conversation.toDict()
                    if user.user_info:
                        other_user.update(user.user_info.chatInfo()) #append the user info and the conversation data
                    chats.append(other_user)
        else:
            chats.append(conversation.toDict()) #else its a group chat so just append the conversations info
    return chats
