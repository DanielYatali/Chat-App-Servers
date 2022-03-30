from email.policy import default
from App.database import db

class User_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    faculty = db.Column(db.String(120))
    major = db.Column(db.String(120))
    user_info = db.Column(db.JSON, default = {})

    def __init__(self, user_info, user_id, major, faculty):
        self.user_info = user_info
        self.user_id = user_id
        self.faculty = faculty
        self.major = major

    def toDict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'faculty': self.faculty,
            'major': self.major,
            'user_info_json': self.user_info,
        }


