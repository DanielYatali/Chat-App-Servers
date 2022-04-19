import email
from App.models import User_info, User, Conversation, message
from App.models import db


def create_bot(user_data):
    user = User.query.get(user_data['user_id'])
    if not user:
        return{
            "message": f"{user_data['user_id']} does not exist"
        }
    if user.user_info:
        return{
            "message": "bot already exist"
        }
    new_user_info = User_info(user_id = user_data['user_id'],first_name=user_data['first_name'], last_name=user_data['last_name'], email = user_data['email'], country=user_data['country'], city = user_data['city'], university=user_data["university"],faculty=user_data['faculty'], major=user_data['major'],movie_type = user_data['movie'], music_type = user_data['music'], sport = user_data['sport'],about=user_data['about'], staying_in=user_data['staying_in'], bot="bot", other_info= user_data['other_info'], photo = user_data['photo'])
    db.session.add(new_user_info)
    user.user_info = new_user_info

    db.session.commit()
    return{
        "message": "bot info added"
    }

def create_user_info(user_data):
    user = User.query.get(user_data['user_id'])
    if not user:
        return{
            "message": "user does not exist"
        }
    if user.user_info:
        return{
            "message": "user_info already exist"
        }
    new_user_info = User_info(user_id = user_data['user_id'],first_name=user_data['first_name'], last_name=user_data['last_name'], email = user_data['email'], country=user_data['country'], city = user_data['city'], university=user_data["university"],faculty=user_data['faculty'], major=user_data['major'],movie_type = user_data['movie'], music_type = user_data['music'], sport = user_data['sport'],about=user_data['about'], staying_in=user_data['staying_in'], bot=user_data['bot'], photo=user_data['photo'] ,other_info= user_data['other_info'])
    db.session.add(new_user_info)
    user.user_info = new_user_info

    db.session.commit()
    return{
        "message": "user info added"
    }

def get_user_info(user_id):
    user = User.query.get(user_id)
    if not user:
        return{
            "message": "user does not exist"
        }
    if not user.user_info:
        return{
            "message": "user_info does not exist",
            "user_id": user_id
        }
    return user.user_info.toDict()
def create_update_user_info(user, user_data):
    if not user.user_info:
        return create_user_info(user_data)
    else:
        return update_user_info(user_data)
        
def update_user_info(user_data):
    old_user = User.query.get(user_data['user_id'])
    if not old_user:
        return{
            "message": "user does not exist"
        }
    
    if not old_user.user_info:
        return{
            "message": "user_info does not exist"
        }
    old_user.user_info.other_info = user_data['other_info']
    old_user.user_info.first_name = user_data['first_name']
    old_user.user_info.last_name = user_data['last_name']
    old_user.user_info.email = user_data['email']
    old_user.user_info.country = user_data['country']
    old_user.user_info.city = user_data['city']
    old_user.user_info.about = user_data['about']
    old_user.user_info.university = user_data['university']
    old_user.user_info.faculty = user_data['faculty']
    old_user.user_info.major = user_data['major']
    old_user.user_info.movie_type = user_data['movie']
    old_user.user_info.music_type = user_data['music']
    old_user.user_info.photo = user_data['photo']
    old_user.user_info.staying_in = user_data['staying_in']
    old_user.user_info.sport = user_data['sport']
    old_user.user_info.bot = user_data['bot']
    db.session.add(old_user)
    db.session.commit()
    return{
        "message": "user info updated"
    }

def match(user_id):
    current_user = User.query.get(user_id)
    if not current_user:
        return{
            "message": "user does not exist"

        }
    if not current_user.user_info:
        return{
            "message": "you must add user info before you can match"
        }
    user_info = current_user.user_info
    #Join groups based on selected criteria for the group
    if not join_match_groups(current_user, user_info.faculty, user_info.sport,user_info.music_type, user_info.movie_type):
        return{
            "message": f"Error invalid group match {user_info.faculty, user_info.sport,user_info.music_type, user_info.movie_type}"
        }
    matches = []
    first_query = User_info.query.filter(User_info.faculty == current_user.user_info.faculty, User_info.user_id != current_user.id);
    second_query = first_query.filter(User_info.major == current_user.user_info.major).limit(5)
    
    if not second_query:
        third_query = first_query.query.all().limit(5)
        matches = [query.toDict() for query in third_query]
    else:    
        matches = [query.toDict() for query in second_query]
    if second_query.count() < 3:
        for info in first_query: 
            #limited to a max of 4 matches
            if len(matches) >= 4:
                break;
            if info not in second_query:
                matches.append(info.toDict())    
    if not first_query:
        return{
            "message": "Sorry no matches yet, please check back later!"
        }
    return matches

def join_match_groups(user, faculty, sport, music, movie): 
    faculty_found = False
    sport_found = False
    music_found = False
    movie_found = False

    #search for groups
    faculty_conversation = Conversation.query.filter_by(criteria = faculty).first()
    sport_conversation = Conversation.query.filter_by(criteria = sport).first()
    music_conversation = Conversation.query.filter_by(criteria = music).first()
    movie_conversation = Conversation.query.filter_by(criteria = movie).first()

    if not faculty_conversation or not sport_conversation or not music_conversation or not movie_conversation:
        return False

    #check if user has already joined these groups
    if user.conversations:
        for conversation in user.conversations:
            if conversation.conversation_name == faculty_conversation:
                faculty_found = True
            if conversation.conversation_name == sport_conversation:
                sport_found = True
            if conversation.conversation_name == music_conversation:
                music_found = True
            if conversation.conversation_name == movie_conversation:
                movie_found = True

    #appending the conversation if user has not joined
    if not faculty_found:
        user.conversations.append(faculty_conversation)
    if not sport_found:
        user.conversations.append(sport_conversation)
    if not movie_found:
        user.conversations.append(movie_conversation)
    if not music_found:
        user.conversations.append(music_conversation)

    db.session.commit()

    return True
