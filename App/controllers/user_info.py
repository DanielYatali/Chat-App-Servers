from App.models import User_info, User
from App.models import db

def create_user_info(user_id, user_info):
    user = User.query.get(user_id)
    if not user:
        return{
            "message": "user does not exist"
        }
    if user.user_info:
        return{
            "message": "user_info already exist"
        }
    new_user_info = User_info(user_id = user_id,faculty=user_info['faculty'], major=user_info['major'],user_info= user_info)
    db.session.add(new_user_info)
    user.user_info = new_user_info
    #if this does not work then add user back to db
    db.session.commit()
    return{
        "message": "user info added"
    }

def get_user_info(user_id):
    # user_info = User_info.query.filter_by(user_id = user_id).first()
    user = User.query.get(user_id)
    if not user:
        return{
            "message": "user does not exist"
        }
    if not user.user_info:
        return{
            "message": "user_info does not exist"
        }
    return user.toDict_info()

def update_user_info(user_id, user_info_json):
    # old_user_info = User_info.query.filter_by(user_id = user_id).first()
    old_user = User.query.get(user_id)
    if not old_user:
        return{
            "message": "user does not exist"
        }
    
    if not old_user.user_info:
        return{
            "message": "user_info does not exist"
        }
    old_user.user_info.user_info = user_info_json
    old_user.user_info.faculty = user_info_json['faculty']
    old_user.user_info.major = user_info_json['major']
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
    matches = {}
    counter = 0
    first_query = User_info.query.filter_by(major = current_user.user_info.major, faculty = current_user.user_info.faculty);
    
    if not first_query or first_query.count() == 1:
        return{
            "message": "hard luck m8, no matches yet"
        }
    for query in first_query:
        if query.user.id != user_id:
            matches[counter] = query.user.toDict_info()
            counter += 1
    
    matches[-1] = counter
    return matches
    # second_query = None
    # if(first_query.count() < 5):
    #     second_query = User_info.query.filter_by(faculty = current_user.user_info.faculty)
    
    # current_user_info = current_user.toDict()
    # for user in users:
    #     user_info = user.

