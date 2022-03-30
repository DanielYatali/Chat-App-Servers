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
    new_user_info = User_info(user_id = user_id, user_info= user_info)
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
    db.session.add(old_user)
    db.session.commit()
    return{
        "message": "user info updated"
    }
