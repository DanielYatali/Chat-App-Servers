from App.models import User, message
from App.database import db

def get_user_id(username):
    user = User.query.filter_by(username = username).first()
    if not user:
        return {"message": "user does not exist"}
    return user.id

def get_all_users():
    return User.query.all()

def create_user(username, email, password):
    newuser = User(username=username, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def signup(username,email, password):
  olduser = User.query.filter_by(username=username).first()  

  if not olduser:
      olduser = User.query.filter_by(email=email).first()

  if olduser:
    return "username or email already exists"
  else:
      create_user(username, email, password)
      return "user created"