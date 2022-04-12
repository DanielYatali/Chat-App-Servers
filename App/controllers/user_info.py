import email
from App.models import User_info, User
from App.models import db


def create_bot(user_data):
    user = User.query.get(user_data['user_id'])
    if not user:
        return{
            "message": "user does not exist"
        }
    if user.user_info:
        return{
            "message": "user_info already exist"
        }
    new_user_info = User_info(user_id = user_data['user_id'],first_name=user_data['first_name'], last_name=user_data['last_name'], email = user_data['email'], country=user_data['country'], city = user_data['city'], university=user_data["university"],faculty=user_data['faculty'], major=user_data['major'],movie_type = user_data['movie'], music_type = user_data['music'], sport = user_data['sport'],about=user_data['about'], staying_in=user_data['staying_in'], bot=user_data['bot'], other_info= user_data['other_info'])
    db.session.add(new_user_info)
    user.user_info = new_user_info

    db.session.commit()
    return{
        "message": "user info added"
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
            "message": "user_info does not exist"
        }
    return user.user_info.toDict()

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
    first_query = User_info.query.filter(User_info.major == current_user.user_info.major, User_info.faculty == current_user.user_info.faculty, User_info.user_id != current_user.id);
    
    if not first_query or first_query.count() == 1:
        return{
            "message": "hard luck m8, no matches yet"
        }
    matches = [query.toDict() for query in first_query]  
    return matches

